"""Local Markdown documentation and router-integrity checks (no runtime claims)."""
from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')


class RepositoryIntegrityTests(unittest.TestCase):
    def test_all_local_markdown_links_resolve(self):
        broken=[]
        for doc in ROOT.rglob('*.md'):
            if doc.name.endswith('.template.md'):
                continue  # Template placeholders are not resolvable links until populated.
            data=doc.read_text(encoding='utf-8')
            # Ignore fenced code examples and literal inline-code snippets.
            lines=[]
            fenced=False
            for line in data.splitlines():
                if line.lstrip().startswith(('```','~~~')):
                    fenced=not fenced
                    continue
                if not fenced:
                    lines.append(line)
            for ref in LINK.findall('\n'.join(lines)):
                path = ref.split('#')[0].strip().split(' "')[0]
                if not path or re.match(r'^[a-z]+:',path) or path.startswith(('/', '#')):
                    continue
                target=(doc.parent/unquote(path)).resolve()
                if not target.exists():
                    broken.append(f'{doc.relative_to(ROOT)} => {ref}')
        self.assertFalse(broken,'Broken local links:\n'+'\n'.join(broken))

    def test_reusable_documentation_is_project_agnostic(self):
        # Guard against leaking local workspace details into portable guidance.
        reusable_paths = [
            ROOT / 'README.md', ROOT / 'AGENTS.md',
            *(ROOT / 'docs').glob('*.md'),
            *(ROOT / 'workflows').glob('*.md'),
            *(ROOT / 'playbook').rglob('*.md'),
            ROOT / '10-projects' / 'README.md',
            ROOT / 'templates' / 'project-agents.template.md',
        ]
        for doc in reusable_paths:
            text = doc.read_text(encoding='utf-8')
            with self.subTest(document=str(doc.relative_to(ROOT))):
                self.assertNotRegex(text, r'(?i)\bsysu(?:-[a-z]+)?\b')
                self.assertNotRegex(text, r'(?i)\bxyver\b')
                self.assertNotRegex(text, r'(?i)[a-z]:\\users\\[^\\\s]+')

    def test_project_agnostic_policy_is_explicit(self):
        agents = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('project-agnostic', agents)
        self.assertIn('project-agnostic', readme)
        self.assertIn('project-specific', readme)

    def test_all_commands_linked_and_workflow_exists(self):
        agents=(ROOT/'AGENTS.md').read_text(encoding='utf-8')
        router=(ROOT/'workflows'/'README.md').read_text(encoding='utf-8')
        for cmd in ['use developer-second-brain','save-progress','resume-progress','sync-knowledge','brain-status']:
            self.assertIn(cmd,agents)
            self.assertIn(cmd,router)
        self.assertIn('development-lifecycle.md',agents)
        self.assertIn('development-lifecycle.md',router)
        self.assertTrue((ROOT/'docs'/'acceptance-tests.md').exists())
        self.assertTrue((ROOT/'workflows'/'project-bootstrap.md').exists())
        self.assertTrue((ROOT/'workflows'/'documentation-modernization.md').exists())
        self.assertTrue((ROOT/'docs'/'documentation-migration.md').exists())
        for trigger in ['audit-docs','migrate-docs']:
            self.assertIn(trigger, agents)
            self.assertIn(trigger, router)

    def test_documentation_migration_requires_explicit_approval(self):
        workflow = (ROOT/'workflows'/'documentation-modernization.md').read_text(encoding='utf-8')
        self.assertIn('Read-only', workflow)
        self.assertIn('STOP and request approval', workflow)
        self.assertIn('source', workflow)
        self.assertIn('10-projects/', workflow)
        self.assertIn('audit-docs', workflow)
        self.assertIn('migrate-docs', workflow)
        template = (ROOT/'templates'/'documentation-audit.template.md').read_text(encoding='utf-8')
        self.assertIn('file', template.lower())
        self.assertIn('Approval needed', template)

    def test_project_template_is_distinct_and_renderable(self):
        template=(ROOT/'templates'/'project-agents.template.md').read_text(encoding='utf-8')
        self.assertTrue((ROOT/'AGENTS.md').read_text(encoding='utf-8').startswith('# Developer Second Brain'))
        self.assertIn('Repository Engineering Instructions',template)
        self.assertEqual(1,template.count('{{SECOND_BRAIN_RELATIVE_PATH}}'))
        self.assertIn('workflows/project-bootstrap.md',template)
        self.assertIn('audit-docs',template)
        self.assertIn('migrate-docs',template)
        self.assertIn('workflows/documentation-modernization.md',template)
        self.assertNotIn('{{SECOND_BRAIN_RELATIVE_PATH}}',template.replace('{{SECOND_BRAIN_RELATIVE_PATH}}','../developer-second-brain'))


if __name__ == '__main__':
    unittest.main()
