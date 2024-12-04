from random import randint


WELCOME = 'Угадайте число от 1 до 100!'


number = randint(1, 100)
print(WELCOME)



def test():
    while True:
        guess = int(input('Введите чило: '))

        if guess < number:
            print('Ваше число меньше')
        

        elif guess > number:
            print('Ваше число больше')
        

        elif guess == number:        
            print('Вы угодали число')
        
            break


test()

print('Отлично! Вы угодали число')
