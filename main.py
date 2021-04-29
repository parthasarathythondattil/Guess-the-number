import random

ran_num = random.randint(0, 101)
attempts = 1
guess = int(input('Enter the guess here >> '))
win = True
while guess != ran_num:
    if attempts == 10:
        win = False
        break
    if guess < ran_num:
        print(f"{guess} is smaller than the number")
    else:
        print(f"{guess} is greater than the number")
    attempts += 1
    print('Try again')
    guess = int(input('Enter the guess here >> '))


if win:
    print(f"Congratulations {guess} is the answer and you got it after {attempts} attempts that's great")
else:
    print(f'You tried your best and the number is {ran_num}')
