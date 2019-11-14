from random import randint
n = randint(1, 200)
#guess = int(input("Enter a number from 1 to 200: "))
guess=''
while n != guess:
    try:
        guess = int(input("Enter a number from 1 to 200: "))
        if guess < n:
            print("Too Low")
        elif guess > n:
            print("Too high")
        elif guess == n:
            print("Nicely done!")
    except NameError as e:
        if e: 
            print('Numbers only please.')
            continue