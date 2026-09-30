import math 
from .flat import circle_area

def sphere_volume(r): return 4 / 3 * math.pi * r ** 3
def cube_volume(a):   return a ** 3
def hemishere_area(r): 
    '''Пакет geometry: плоские и пространственные фигуры.'''
    return 2 * math.pi ** 2 + circle_area(r)
