import ast
from pathlib import Path
SOURCE=(Path(__file__).parents[1]/'contracts'/'contract.py').read_text()
TREE=ast.parse(SOURCE)
def load(name):
 node=next(x for x in TREE.body if isinstance(x,ast.FunctionDef) and x.name==name)
 scope={};exec(compile(ast.Module(body=[node],type_ignores=[]),'<contract>','exec'),scope);return scope[name]
def test_precedent_conflict_is_decision_sensitive():
 fn=load('precedent_conflict');assert fn('GRANT',['GRANT']) is False;assert fn('DENY',['GRANT']) is True
def test_surface_and_consensus_fields():
 for name in ('open_book','file_case','evaluate','get_book','get_case'):assert f'def {name}' in SOURCE
 assert 'prompt_comparative' in SOURCE and 'both digests must match exactly' in SOURCE
 assert "origin == book.policy_origin" in SOURCE and "state != 'FILED'" in SOURCE

