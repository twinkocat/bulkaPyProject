import random

def IntInput():
    start=input()
    end=input()
    if start.isdigit() and end.isdigit():
        start=int(start)
        end=int(end)
        ruletka(start, end)
    else:
        print('smth wrong')
        return IntInput()

def ruletka(start, end):
    if start > end:
        print('smth wrong')
        IntInput()
    else:
        print(f'{start} to {end}')
        a = int(input())
        if a > 10:
            print('smth wrong')
            return ruletka(start, end)

        b = random.randint(start, end)
        while b != a:
            print('You lose')
            return ruletka(start, end)
        else:
            print('You won')

print(IntInput())