import mymodule
from mymodule import circle_area, VERSION
from mymodule import circle_len as perimeter
import mymodule as mm

print('1) mymodele.circle_area(5) =', mymodule.circle_area(5))
print('2) circle_area(5) =', cirle_area(5))
print('3) perimeter(5) =', perimeter(5))
print('4) mm.PI =', circle_area(5))

print('dir(mymodule) ->', mymodule.__name__)
print('mymodule.__file__ =', mymodule.__file__)