import ast

class DeadCodeRemover(ast.NodeTransformer):
"""Простейшая вырезка `if False:` блоков и `if 0:`"""
def visit_If(self, node):
self.generic_visit(node)
test = node.test
if isinstance(test, ast.Constant):
if not test.value:
# заменяем на тело orelse (если есть) или удаляем
return node.orelse or []
return node


_jit_cache = {}

def _find_function_node(mod, name):
for node in ast.walk(mod):
if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
return node
return None

def jit_optimize(func=None):
"""Декоратор: оптимизирует и компилирует функцию на лету.

Применение:
@jit_optimize
def f(x):
return (2 + 3) * x


"""
if func is None:
return jit_optimize


if not inspect.isfunction(func):
return func


try:
source = inspect.getsource(func)
except (OSError, IOError, TypeError):
# нельзя получить исходник — возвращаем оригинал
return func

key = (func.__module__, func.__qualname__, source)
if key in _jit_cache:
return _jit_cache[key]

try:
# парсим и оптимизируем AST
mod = ast.parse(source)
func_node = _find_function_node(mod, func.__name__)
if func_node is None:
return func

folder = ConstantFolder()
dcr = DeadCodeRemover()
folder.visit(mod)
dcr.visit(mod)
ast.fix_missing_locations(mod)

# компилируем оптимизированный модуль в новый namespace
globs = func.__globals__.copy()
compiled = compile(mod, filename="<jit-optimized>", mode="exec")
ns = {}
exec(compiled, globs, ns)
new_func = ns.get(func.__name__)
if new_func is None:
return func

try:
functools.update_wrapper(new_func, func)
except Exception:
pass

_jit_cache[key] = new_func
return new_func
except Exception:
# в случае любой ошибки возвращаем исходную функцию
return func

