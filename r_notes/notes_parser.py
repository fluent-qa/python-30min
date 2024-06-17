from jupyter_notebook_parser import JupyterNotebookParser as Parser
from jupyter_notebook_parser import SourceCodeContainer as SourceCode

PY_MD_CODE_TEMPALTE = """
```python
{CODE}
```
"""


class NotesComposer:

    def __init__(self, note_path):
        self.note_path = note_path
        self.parsed = Parser(self.note_path)

    def compose_md_files(self):
        cells = self.parsed.get_all_cells()
        content = []
        for cell in cells:
            if cell['cell_type'] == 'code':
                content.append(PY_MD_CODE_TEMPALTE.format(CODE="".join(cell['source'])))
            if cell['cell_type'] == 'markdown':
                content.append("".join(cell['source']))
        return content


if __name__ == '__main__':
    result = NotesComposer("./itermedia/generators.ipynb").compose_md_files()
    with open("result.md", "w") as f:
        f.writelines(result)
