# print('квадратное уравнение в форме: ax² bx + c')



 try:
    a = int(input('Введите коэффициент a: '))


    if a == 0:
        print(
        'Если a=0, квадратное уравнение не может быть вычислено!')
    else:
        b = int(input('Введите коэффициент b: '))
        c = int(input('Введите коэффициент c: '))
        delta = b * b - (4 * a * c)


        if delta < 0:
            print('Дельта меньше 0. нет корней.')
        elif delta == 0:
            k = -b / (2 * a)
            print('Если Дельта = 0, то корень = ', k)
        else:
            k1 = (-b + math.sqrt(delta)) / (2 * a)
            k2 = (-b - math.sqrt(delta)) / (2 * a)
            print('Корень: \n Корень-1 =', k1, ' \n Корень-2 =', k2)
except Exception as e:
    print("Exception (коэффициент a):", e)
    pass
