a = int(input('Number:'))
if a >= 100 and a <= 999:
    b = a // 100
    n = (a // 10) % 10
    c = a % 10
else:
    print('Error')
v = b + n + c
print(v)

a = int(input('Number:'))
if a >= 100 and a <= 999:
    b = a // 100
    n = (a // 10) % 10
    c = a % 10
else:
    print('Error')
print (c, n, b)

a = int(input('Number:'))
if a >= 100 and a <= 999:
    b = a // 100
    n = a % 100
    print(n, b, sep='')
else:
    print('Error')

a = int(input('Number:'))
if a >= 100 and a <= 999:
    c = a % 10
    v = a % 100
    print(c, v, sep='')

a = int(input('Number:'))
if a >= 100 and a <= 999:
    b = a // 100
    n = a % 100
    print(n, b, sep= '')
else:
    print('Error')