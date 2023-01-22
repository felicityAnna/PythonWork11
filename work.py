# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import matplotlib.pyplot as plt
from sympy import *

# Определение функции 
x = Symbol('x')
func = 18*x**3+5*x**2+10*x-30
y = solve(func)

print('\n 1. Определить корни')
x1 = y[0]
x2 = y[1]
print (f'Первый корень: {x1}')
print (f'Второй корень: {x2}')

fd = diff(func)
print(f'\n 2. Найти интервалы, на которых функция возрастает: ')
print(solve(0 < fd))

print(f'\n 3. Найти интервалы, на которых функция убывает: ')
print(solve(0 > fd))

print("4. Построить график")
list_y = []
for i in range(-5, 6):
    x = i
    y = 5*x**2+10*x-30
    list_y.append(y)
print(list_y)
plt.plot(range(-5, 6), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
plt.plot(range(-5, 6), list_y)
plt.grid()
plt.show()

print(f'\n 5. Вычислить вершину: ')
corni = solve(fd)
x = corni[0]
y = 5*x**2+10*x-30
print(x, y)

print(f'\n 6. Определить промежутки, на котором f > 0: ')
print(solve(0 < func))

print(f'\n 7. Определить промежутки, на котором f < 0: ')
print(solve(func < 0))