import ast
import pathlib


def multiline_fstrings(path="."):
    hits = []
    for p in pathlib.Path(path).rglob("*.py"):
        if "venv" in p.parts or p.name.startswith("."):
            continue
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.JoinedStr):
                if node.lineno != node.end_lineno:
                    hits.append(f"{p}:{node.lineno}")
    return hits


hits = multiline_fstrings()
print(f"Found {len(hits)} multiline f-strings:\n")
print("\n".join(hits))
