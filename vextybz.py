a = float(int(input('Введите число:')))
P = 4 * a
print (P)

a = float(int(input('Введите число:')))
S = a ** 2 
print (S)

a = float(int(input('Введите число:')))
b = float(int(input('Введите число:')))
S = a * b 
P = 2 * (a + b)
print(S, P)

d = float(input("Введите диаметр окружности: "))
pi = 3.14
L = pi * d
print(f"Длина окружности L = {L}")

a = float(int(input('Введите число:')))
V = a ** 3 
S = 6 * a **2
print (V, S)

a = float(int(input('Введите число:')))
b = float(int(input('Введите число:')))
c = float(int(input('Введите число:'))) 
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print (V, S)

R = float(int(input('Введите число:')))
pi = 3.14
L = pi * 2 * R
S = pi * R ** 2
print (L, S)

a = float(int(input('Введите число:'))) 
b = float(int(input('Введите число:')))
sred = (a + b) / 2
print (sred)

import math
a = float(int(input('Введите число:')))
b = float(int(input('Введите число:')))
if a >= 0 and b >= 0:
    geom_mean = math.sqrt(a * b)
    print (geom_mean)
else:
    print('Error')

a = float(int(input('Введите число:')))
b = float(int(input('Введите число:')))
if a >= 0 and b >= 0:
    sred = (a + b) / 2
    proi = a * b 
    proi_2 = a ** 2 * b ** 2
    chast = a ** 2 / b ** 2
    print (sred, proi, proi_2, chast)
else:
    print ('Error')

a = float(int(input('Введите число:'))) 
b = float(int(input('Введите число:')))
if a == 0 or b == 0:
    print ('Error')
else: 
    abs_a = abs(a)
    abs_b = abs(b)
    suma = abs_a + abs_b
    raz = abs_a - abs_b
    proiz = abs_a * abs_b
    chast = abs_a / abs_b
    print(suma, raz, proiz, chast)

import math
a = float(int(input('Введите число:')))
b = float(int(input('Введите число:')))
c = math.sqrt(a ** 2 + b ** 2)
P = a + b + c
print (c, P)

R = float(int(input('Введите число:')))
R_1 = float(int(input('Введите число:')))
pi = 3.14
S = pi * R ** 2
S_1 = pi * R_1 ** 2
S_2 = S - S_1
print (S, S_1, S_2)

L = float(int(input('Введите число:')))
pi = 3.14
R = L / 2 * pi
S = pi * R ** 2
print (R, S)

import math 
S = float(int(input('Введите число:')))
pi = 3.14
R = math.sqrt (S / pi)
L = 2 * pi * R 
print (R, L)

x = float(int(input('Введите число:')))
x_1 = float(int(input('Введите число:')))
distance = abs(x - x_1)
print (distance)

A = float(int(input('Введите число:')))
B = float(int(input('Введите число:')))
C = float(int(input('Введите число:')))
distance = abs(A - B)
distance_1 = abs(B - C)
sum = distance + distance_1
print (distance, distance_1, sum)

A = float(int(input('Введите число:')))
B = float(int(input('Введите число:')))
C = float(int(input('Введите число:')))
distance = abs(A - C)
distance_1 = abs(B - C)
proiz = distance * distance_1
print(proiz)



import math
x1 = float(int(input('Введите число:')))
y1 = float(int(input('Введите число:')))
x2 = float(int(input('Введите число:')))
y2 = float(int(input('Введите число:')))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print (distance)

import math
x1 = float(int(input('Введите число:')))
y1 = float(int(input('Введите число:')))
x2 = float(int(input('Введите число:')))
y2 = float(int(input('Введите число:')))
x3 = float(int(input('Введите число:')))
y3 = float(int(input('Введите число:')))
a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
P = a + b + c
p = P / 2
S = math.sqrt(p * (p - a) * (p - b) * (p-c))
print (S, P)

a = float(int(input('Введите число:')))
b = float(int(input('Введите число:')))
a, b = b, a
print(a, b)

a = float(int(input('Введите число')))  
b = float(int(input('Введите число'))) 
c = float(int(input('Введите число')))
a, b, c = b, c, a
print (a, b, c)

a = 1
b = 2
c = 3
a, b, c = b, c, a
print (a, b, c)

def calculate_y(x):
    y = 3 * (x ** 6) - 6 * (x ** 2) - 7
    return y 
x_value = 2
result = calculate_y(x_value)
print(x_value, result)

x = float(int(input))
t = (x - 3) ** 3
y = 4 * (t ** 2) - 7 * t + 2
print (x, y)

A = float(input("Введите число A: "))
a2 = A * A
print(a2)
a4 = a2 * a2
print (a4)
a8 = a4 * a4
print (a8)

A = float(input("Введите число A: "))
a2 = A * A
a3 = a2 * A
a5 = a3 * a2
a10 = a5 * a5
a15 = a10 * a5
print (a15)

alpha = 45
pi = 3.14
if 0 < alpha < 360:
    rad = alpha * (pi/180)
    print (rad)
else:
    print ('error')

alpha = 50
pi = 3.14
alpha_deg = alpha * 180 / pi
print (alpha_deg)

tf = float(input("Введите температуру в градусах Фаренгейта: "))
tc = (tf - 32) * 5 / 9
print (tc)

tc = float(input("Введите температуру в градусах Цельсия: "))
tf = tc * 9 / 5 + 32
print (tf)

x = float(input("Введите вес конфет в кг (X): "))
a = float(input("Введите стоимость X кг конфет в рублях (A): "))
y = float(input("Введите вес для расценки в кг (Y): "))
price_per_kg = a / x
price_y_kg = price_per_kg * y
print (price_per_kg, price_y_kg)

X = float(input("Введите вес шоколадных конфет (кг): "))
A = float(input("Введите стоимость шоколадных конфет (руб): "))
Y = float(input("Введите вес ирисок (кг): "))
B = float(input("Введите стоимость ирисок (руб): "))
price_per_kg_chocolate = A / X
price_per_kg_toffee = B / Y
ratio = price_per_kg_chocolate / price_per_kg_toffee
print(price_per_kg_chocolate, price_per_kg_toffee, ratio)

def calculate_distance(v, u, t1, t2):
     if u >= v:
        return "Ошибка: скорость течения должна быть меньше скорости лодки (U < V)."
s_lake = v * t1
s_river = (v - u) * t2
s_total = s_lake + s_river
return s_total
try:
    v = float(input("Введите скорость лодки в стоячей воде (V, км/ч): "))
    u = float(input("Введите скорость течения реки (U, км/ч): "))
    t1 = float(input("Введите время движения по озеру (T1, ч): "))
    t2 = float(input("Введите время движения против течения (T2, ч): "))
    result = calculate_distance(v, u, t1, t2)
    
    if isinstance(result, str):
        print(result)
    else:
        print(result)

except ValueError:
    print(Error)

def calculate_distance_apart(v1, v2, s, t):
   total_speed = v1 + v2
   distance_traveled = t * total_speed
   final_distance = s + distance_traveled
   return final_distance
v1 = 60
v2 = 80   
s = 20
t = 2
result = result = calculate_distance_apart(v1, v2, s, t)
print(t, result)

v1 = float(input("Введите скорость первого автомобиля (V1, км/ч): "))
v2 = float(input("Введите скорость второго автомобиля (V2, км/ч): "))
s = float(input("Введите начальное расстояние (S, км): "))
t = float(input("Введите время движения (T, часов): "))
total_speed = v1 + v2
total_distance_covered = t * total_speed
final_distance = abs(s - total_distance_covered)
print(t, final_distance)

def solve_linear_equation(a: float, b: float) -> float:
    if a == 0:
        raise ValueError("Коэффициент A не должен быть равен 0.")
    return -b / a


import math
A = float(input("Введите коэффициент A (не равный 0): "))
B = float(input("Введите коэффициент B: "))
C = float(input("Введите коэффициент C: "))
D = B**2 - 4 * A * C
root1 = (-B + math.sqrt(D)) / (2 * A)
root2 = (-B - math.sqrt(D)) / (2 * A)
min_root = min(root1, root2)
max_root = max(root1, root2)
print(min_root)
print(max_root)

a1 = float(input("Введите коэффициент A1: "))
b1 = float(input("Введите коэффициент B1: "))
c1 = float(input("Введите коэффициент C1: "))
a2 = float(input("Введите коэффициент A2: "))
b2 = float(input("Введите коэффициент B2: "))
c2 = float(input("Введите коэффициент C2: "))
d = a1 * b2 - a2 * b1
if d == 0:
  print("Система не имеет единственного решения (D = 0).")
else:
      x = (c1 * b2 - c2 * b1) / d
      y = (a1 * c2 - a2 * c1) / d
      print (x, y)