import random


def int_input():
    """Ввод с проверкой и присваиванием численного значения"""
    start = input("Первое число: ")
    end = input("Второе число: ")

    if start.isdigit() and end.isdigit():
        start, end = int(start), int(end)
    else:
        print('Необходимо указать целочисленное значение для первого и второго числа.')
        return int_input()

    if start >= end:
        print('Первое число не может быть равно или больше второго')
        int_input()
    else:
        print(f'Введите число от {start} до {end}:')
        random_game(start, end)


def random_game(start, end):
    """ Тело программы: создание диапазона случайных чисел из ранее вводимых;
        ввод числа "a" пользователем с проверкой, что оно в диапазоне наших значений, а так-же быть числом;
    """
    a = input()

    if a.isdigit():
        a = int(a)
    else:
        print("Вводимое Вами поле должно быть ЧИСЛОМ")
        return random_game(start, end)

    if a < start or a > end:
        print(f"Число должно быть в диапазоне от {start} до {end}")
        return random_game(start, end)

    b = random.randint(start, end)

    while b != a:
        print('Попробуйте еще раз!')
        return random_game(start, end)
    else:
        print('Вы угадали!')


print(int_input())
