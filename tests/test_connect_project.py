"""Offline, standard-library checks for the optional AGENTS.md bridge helper."""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'connect-project.py'


class ConnectProjectTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.project = Path(self.tmp.name) / 'sample-app'
        self.project.mkdir()

    def invoke(self,*args):
        return subprocess.run([sys.executable,str(SCRIPT),'--project',str(self.project),*args],
                              capture_output=True,text=True,check=False)

    def test_full_template_preview_does_not_write(self):
        result = self.invoke('--full-template')
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn('Repository Engineering Instructions', result.stdout)
        self.assertFalse((self.project/'AGENTS.md').exists())

    def test_full_template_apply_renders_vault_path(self):
        result = self.invoke('--full-template','--apply')
        self.assertEqual(0,result.returncode,result.stderr)
        output = (self.project/'AGENTS.md').read_text(encoding='utf-8')
        self.assertIn('Repository Engineering Instructions',output)
        self.assertIn('workflows/project-bootstrap.md',output)
        self.assertIn('audit-docs',output)
        self.assertIn('migrate-docs',output)
        self.assertNotIn('{{SECOND_BRAIN_RELATIVE_PATH}}',output)
        self.assertIn('developer-second-brain',output)
        self.assertFalse((self.project/'CLAUDE.md').exists())

    def test_full_template_refuses_to_overwrite(self):
        p=self.project/'AGENTS.md'
        p.write_text('# Custom AGENTS\nUser rules must remain.\n',encoding='utf-8')
        result=self.invoke('--full-template','--apply')
        self.assertNotEqual(0,result.returncode)
        self.assertIn('Existing AGENTS.md',result.stderr)
        self.assertEqual('# Custom AGENTS\nUser rules must remain.\n',p.read_text(encoding='utf-8'))

    def test_second_full_template_apply_is_safe_and_no_churn(self):
        self.assertEqual(0,self.invoke('--full-template','--apply').returncode)
        p=self.project/'AGENTS.md'
        first=p.read_bytes()
        self.assertNotEqual(0,self.invoke('--full-template','--apply').returncode)
        self.assertEqual(first,p.read_bytes())

    def test_symlinked_agents_file_is_rejected(self):
        actual = Path(self.tmp.name) / 'external-agents.md'
        actual.write_text('# Outside instructions\n', encoding='utf-8')
        link = self.project / 'AGENTS.md'
        try:
            link.symlink_to(actual)
        except (OSError, NotImplementedError) as exc:
            self.skipTest(f'Symlinks unavailable: {exc}')
        self.assertNotEqual(0, self.invoke('--apply').returncode)
        self.assertNotEqual(0, self.invoke('--refresh', '--apply').returncode)
        self.assertNotEqual(0, self.invoke('--full-template', '--apply').returncode)
        self.assertEqual('# Outside instructions\n', actual.read_text(encoding='utf-8'))

    def test_full_template_cannot_refresh(self):
        result=self.invoke('--full-template','--refresh')
        self.assertNotEqual(0,result.returncode)
        self.assertFalse((self.project/'AGENTS.md').exists())

    def test_preview_does_not_write(self):
        p = self.invoke()
        self.assertEqual(0,p.returncode,p.stderr)
        self.assertFalse((self.project/'AGENTS.md').exists())

    def test_apply_creates_and_is_idempotent(self):
        self.assertEqual(0,self.invoke('--apply').returncode)
        target = self.project/'AGENTS.md'
        value = target.read_text(encoding='utf-8')
        self.assertIn('development-lifecycle.md',value)
        self.assertIn('audit-docs',value)
        self.assertIn('migrate-docs',value)
        self.assertEqual(0,self.invoke('--apply').returncode)
        self.assertEqual(value,target.read_text(encoding='utf-8'))

    def test_existing_instructions_preserved(self):
        p = self.project/'AGENTS.md'
        p.write_text('# Existing rules\nKeep these.\n',encoding='utf-8')
        result = self.invoke('--apply')
        self.assertEqual(0,result.returncode,result.stderr)
        self.assertTrue(p.read_text(encoding='utf-8').startswith('# Existing rules\nKeep these.\n'))

    def test_malformed_markers_rejected(self):
        p = self.project/'AGENTS.md'
        p.write_text('<!-- developer-second-brain:begin -->',encoding='utf-8')
        result=self.invoke('--refresh','--apply')
        self.assertNotEqual(0,result.returncode)
        self.assertEqual('<!-- developer-second-brain:begin -->',p.read_text(encoding='utf-8'))

    def test_v11_legacy_block_requires_explicit_refresh(self):
        from_text = ('# My rules\n\n<!-- developer-second-brain:begin -->\n'
                     'old V1.1 instructions\n<!-- developer-second-brain:end -->\n\n# More rules\n')
        p=self.project/'AGENTS.md'
        p.write_text(from_text,encoding='utf-8')
        result=self.invoke('--apply')
        self.assertEqual(0,result.returncode)
        self.assertEqual(from_text,p.read_text(encoding='utf-8'))
        preview=self.invoke('--refresh')
        self.assertEqual(0,preview.returncode,preview.stderr)
        self.assertIn('development-lifecycle.md',preview.stdout)
        self.assertEqual(from_text,p.read_text(encoding='utf-8'))
        applied=self.invoke('--refresh','--apply')
        self.assertEqual(0,applied.returncode,applied.stderr)
        new=p.read_text(encoding='utf-8')
        self.assertIn('development-lifecycle.md',new)
        self.assertTrue(new.startswith('# My rules\n\n'))
        self.assertTrue(new.endswith('\n\n# More rules\n'))

    def test_duplicate_markers_rejected(self):
        p=self.project/'AGENTS.md'
        p.write_text(('<!-- developer-second-brain:begin -->' * 2 +
                      '<!-- developer-second-brain:end -->'),encoding='utf-8')
        result=self.invoke('--refresh','--apply')
        self.assertNotEqual(0,result.returncode)

    def test_no_routing_for_nonexistent_project(self):
        p=self.project/'AGENTS.md'
        self.project.rmdir()
        result=self.invoke('--apply')
        self.assertNotEqual(0,result.returncode)
        self.assertFalse(p.exists())

    def test_updates_preserve_utf8_bom_and_crlf(self):
        p=self.project/'AGENTS.md'
        p.write_bytes(b'\xef\xbb\xbf# Legacy\r\n')
        first=self.invoke('--apply')
        self.assertEqual(0,first.returncode,first.stderr)
        content=p.read_bytes()
        self.assertTrue(content.startswith(b'\xef\xbb\xbf'))
        self.assertIn(b'\r\n',content)
        second=self.invoke('--refresh','--apply')
        self.assertEqual(0,second.returncode,second.stderr)
        self.assertEqual(content,p.read_bytes())


if __name__ == '__main__':
    unittest.main()
