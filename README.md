# MyFastLib
![Uploading 2025-12-25_17-55-41.png…]()

Version 1.2.5

Обновление ZIP архиватора 
Пример использования: 

myfast zip data data.zip
myfast unzip data.zip out
myfast tar logs logs.tar.gz
myfast bench test.py


🚀 MyFastLib — ультра-лёгкая библиотека для ускорения Python-кода

MyFastLib — это компактная, модульная и понятная библиотека, созданная для того, чтобы сделать Python быстрее без лишней магии и зависимости от тяжёлых JIT-движков.

Библиотека включает:

⚡ JIT-оптимизатор на уровне AST (constant folding, dead code removal)

🔥 Мини-байткод оптимизатор (byteJIT)

🧠 Утилиты для параллелизма и ускорения задач

📦 Простую структуру, которую легко расширять под свои нужды

Создано программистом, который устал от медленных циклов и решил сделать мини-Nuitka/PyPy на коленке

#✨ Возможности

🔥 JIT AST Optimizer — @jit_optimize

- Оптимизирует код на стадии AST:
- свёртка констант
- упрощение выражений
- удаление мёртвых веток
- компиляция оптимизированной версии функции

⚙️ Bytecode Optimizer — @bytejit

Мини-оптимизатор Python-байткода:

peephole-оптимизации

упрощение LOAD_CONST / BINARY_OP

инлайнинг вычисляемых констант

from myfastlib.bytejit import bytejit

@bytejit
def f():
    return 10 + 20  # → оптимизируется в LOAD_CONST 30

🧵 Параллельные операции в utils

Ускорение типичных задач:

from myfastlib.utils import parallel_map

result = parallel_map(lambda x: x*x, range(10), workers=4)

📁 Структура проекта
myfastlib/
│── __init__.py
│── utils.py
│── jit.py
│── bytejit.py
└── fastmath.py
README.md

📦 Установка

pip install myfastlib==1.0.1

pip install myfastlib


Пока локально:

git clone https://github.com/yourname/myfastlib
cd myfastlib

🧪 Тестирование
python -m tests

💡 Примеры ускорения
До:
def f():
    return (10 + 20) * (5 - 2)

После JIT:

выражения свёрнуты
- код легче
- байткод проще

🛠 План развития

 JIT-кэширование между запусками

 - Оптимизация циклов
 - Fusion операций (как у NumPy)
 -  Мини IR (собственный слой промежуточного представления)
  - Генерация C-кода через CFFI

🤝 Контрибьютинг

Открыт для идей, PR и предложений. Можно улучшать опкоды, оптимизаторы, AST-трансформации и многое другое.

⭐ Поддержи проект

Если библиотека полезна — поставь ⭐ на GitHub.
Это помогает развитию проекта!
