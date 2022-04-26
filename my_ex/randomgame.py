import random

def IntInput():
    start=input("Первое число: ")
    end=input("Второе число: ")
    if start.isdigit() and end.isdigit():
        start, end = int(start), int(end)
        ruletka(start, end)
    else:
        print('Необходимо указать целочисленное значение.')
        return IntInput()

def ruletka(start, end):
    if start >= end:
        print('Первое число не может быть равно или больше второго')
        IntInput()
    else:
        print(f'Введите число от {start} до {end}:')
        a = int(input())
        if a > end:
            print(f'Введите значение в диапазоне от {start} до {end}')
            return ruletka(start, end)

        b = random.randint(start, end)
        while b != a:
            print('Попробуйте еще раз!')
            return ruletka(start, end)
        else:
            print('Вы угадали!')
print(IntInput())
