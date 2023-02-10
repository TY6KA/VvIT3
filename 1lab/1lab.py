import math
b, a, c = map(int, input().split())
D = b ** 2 - 4 * a * c
if a == 0 or b == 0 or c == 0:
    print('Корней нет')
elif D < 0 or b == 0 or a == 0 or c == 0:
    print('Корней нет')
elif D == 0:
    print(f'{(-b) / (2 * a)}')
else:
    x1 = (-b + (math.sqrt(D) / 2 * a))
    x2 = (-b - (math.sqrt(D) / 2 * a))
    print(round(x1, 1), round(x2, 1))

