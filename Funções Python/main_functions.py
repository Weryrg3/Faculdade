x = 10
y = 5
x + y == 15         # Adição
x - y == 5          # Subtranção
x * y == 50         # Multiplicação
x / y == 2.0        # Divisão (float)
x // y == 2         # Divisão (inteira)
x % y == 0          # Resto da divisão
-x == -10           # operador negativo
+x == 10            # operador positivo
x ** y == 100000    # Elevação
x, y = 3, 4         # x = 3, y = 4
x, y = [3, 4]       # x = 3, y = 4
x, *y = [3, 4, 5]   # x = 3, y = [4, 5]

# bits
x | y == 15
x ^ y == 15
x & y == 0
x << y == 320
x >> y == 0
~x == -11


# condição bool
or and if elif else is not False True

# loop
break for from with in while range()

# Tratamento de erros
try except raise
    # erros
    ArithmeticError      AssertionError      AttributeError          BrokenPipeError         BlockingIOError
    BufferError          ChildProcessError   ConnectionRefusedError  ConnectionAbortedError  ConnectionResetError 
    ConnectionError      EOFError            EnvironmentError        FileNotFoundError       FileExistsError 
    FloatingPointError   IOError             IndentationError        IsADirectoryError       ImportError 
    IndexError           InterruptedError    KeyError                LookupError             MemoryError
    ModuleNotFoundError  NameError           NotADirectoryError      NotImplementedError     OSError 
    OverflowError        ProcessLookupError  PermissionError         RecursionError          ReferenceError
    RuntimeError         SyntaxError         SystemError             TabError                TimeoutError 
    TypeError            UnboundLocalError   UnicodeTranslateError   UnicodeDecodeError      UnicodeEncodeError
    UnicodeError         ValueError          ZeroDivisionError

# listas 
in del

# classe ou funções
class def return continue import

# desconhecidos
as assert exec() finally global lambda nonlocal pass yield 

abs(10.50)                  # 10.50 Return the absolute value of a number.
all([True, False])          # False
any([True, False])          # True
ascii()
bin(3)                      # 0b11
bool(0)                     # False
bytearray()
bytes()
callable()
chr(65)                     # A
classmethod()
compile()
complex("1+2j")             # (1+2j)
copyright()
credits()
delattr()
dict()
dir()
divmod(10, 2)               # (5, 0) Retorna divisão e resto
enumerate([1, 2, 3])        # <enumerate object at 0x7f09352221f8>
    list(enumerate(...))    # [(0, 1), (1, 2), (2, 3)]
eval("x + 10")              # 20
exit()
filter()
float(10)                   # 10.0
format(10, "x")             # a
    (1555, "o")             # 3023
    (15, "E")               # 1.500000E+01
    (1555, "F")             # 1555.000000

frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex(255)                    # 0xff
    '%#x' % 255, '%x' % 255, '%X' % 255                   # ('0xff', 'ff', 'FF')
    format(255, '#x'), format(255, 'x'), format(255, 'X') # ('0xff', 'ff', 'FF')
    f'{255:#x}', f'{255:x}', f'{255:X}'                   # ('0xff', 'ff', 'FF')

id()
input("teste:")             # teste:
int(10.9)                   # 10
isinstance()
issubclass()
iter()
len("casa")                 # 4
license()
list()
locals()
map()
max([1, 5, 2, 9, 3, 4])     # 9
memoryview()
min([1, 5, 2, 9, 3, 4])     # 1
next()
object()
oct(8)                      # 0o10
    '%#o' % 10, '%o' % 10               # ('0o12', '12')
    format(10, '#o'), format(10, 'o')   # ('0o12', '12')
    f'{10:#o}', f'{10:o}'               # ('0o12', '12')

open("arquivo.txt", "r") # <_io.TextIOWrapper name='arquivo.txt' mode='r' encoding='UTF-8'>
    "r" => # Abre para ler
    "w" => # Abre para escrever, deleta o que estava escrito antes
    "x" => # Cria um novo arquivo
    "a" => # Abre para escrever, escreve no fim do arquivo
    "b" => # modo binário
    "t" => # Modo texto
    "+" => # Abre o disco para update ??
    "U" => # Modo universal de novas linhas (Dep)

ord("A")                   # 65
pow(10, 2)                 # 100 -> 10**2
print("A")                 # A -> com "\n"
    ("A", end="")          # A -> sem "\n"

property()
quit()
range(0, 10)               # range(0, 10) -> list(range(0, 5)) => [0, 1, 2, 3, 4]
repr()
reversed()
round(20.2834, 2)          # 20.28
set()
setattr()
slice()
sorted([2, 3, 1])          # [1, 2, 3]
    ([2, 3, 1], reverse = False) # [3, 2, 1]
staticmethod()
str(10)                    # '10'
sum(1, 2, 3])              # 6
super()
tuple([1, 2, 3])           # (1, 2, 3)
type([1, 2, 3])            # <class 'list'>
vars()
zip([1, 2, 3], [4, 5, 6])  # <zip object at 0x7f0935219b08>
    list(zip(...)) # [(1, 4), (2, 5), (3, 6)]

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
c.conjugate()	

import math
float.is_integer()
# https://docs.python.org/3/library/stdtypes.html#index-13 
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# https://docs.python.org/3/library/functions.html



BaseException()
BytesWarning()
DeprecationWarning()
Ellipsis
Exception()
FutureWarning()
GeneratorExit()
ImportWarning()
KeyboardInterrupt()
None
NotImplemented
PendingDeprecationWarning()
ResourceWarning()
RuntimeWarning()
StopAsyncIteration()
StopIteration()
SyntaxWarning()
SystemExit()
UnicodeWarning()
UserWarning()
Warning()