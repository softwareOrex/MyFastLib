import dis
elif opname == 'BINARY_SUBTRACT':
val = A - B
elif opname == 'BINARY_MULTIPLY':
val = A * B
elif opname in ('BINARY_TRUE_DIVIDE','BINARY_FLOOR_DIVIDE'):
val = A / B
else:
raise Exception('unsupported')
new_ins = types.SimpleNamespace(opname='LOAD_CONST', argval=val, arg=None)
out.append(new_ins)
i += 3
continue
except Exception:
pass
if i+1 < n:
a = instrs[i]
b = instrs[i+1]
if a.opname == 'LOAD_CONST' and b.opname == 'UNARY_NEGATIVE':
try:
val = -a.argval
new_ins = types.SimpleNamespace(opname='LOAD_CONST', argval=val, arg=None)
out.append(new_ins)
i += 2
continue
except Exception:
pass
out.append(types.SimpleNamespace(opname=ins.opname, argval=ins.argval, arg=ins.arg))
i += 1
return out




def byte_optimize(func):
if not _supported:
return func
code = func.__code__
instrs = list(dis.get_instructions(code))
optimized = _peephole_optimize(instrs)
try:
new_code_bytes, new_consts, new_names = _assemble_instructions(optimized)
except Exception:
return func
try:
# co_consts: сохраняем оригинальное first const (обычно docstring)
first = (code.co_consts[0],) if code.co_consts else ()
new_consts_full = first + new_consts
new_co = code.replace(co_code=new_code_bytes, co_consts=new_consts_full, co_names=new_names)
new_func = types.FunctionType(new_co, func.__globals__, func.__name__, argdefs=func.__defaults__, closure=func.__closure__)
try:
functools.update_wrapper(new_func, func)
except Exception:
pass
return new_func
except Exception:
return func


from functools import wraps


def bytejit(func):
"""Декоратор — пытается заменить функцию оптимизированной версией.
Возвращает оригинал при неудаче."""
try:
optimized = byte_optimize(func)
return optimized
except Exception:
return func
