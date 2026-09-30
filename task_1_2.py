import task_1_2
from task_1_2 import circle_area, VERSION
from task_1_2 import circle_len as perimeter
import task_1_2 as mm

print("1) mymodule.circle_area(5) =", task_1_2.circle_area(5))
print("2) circle_area(5)          =", circle_area(5))
print("3) perimeter(5)            =", perimeter(5))
print("4) mm.PI                   =", mm.PM)

print("dir(mymodule) ->", [n for n in dir(task_1_2) if not n.startswith("__")])
print("mymodule.__name__=", task_1_2.__name__)
print("mymodule.__file__=", task_1_2.__file__)

print("mm._helper() =", mm._helper())
