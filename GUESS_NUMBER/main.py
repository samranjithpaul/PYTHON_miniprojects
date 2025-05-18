import random

print ("HEY FIRST YOU PLAY THEN ME,play hard")

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'\n\n guess a number between 1 and {x}: '))
    
        if guess < random_number:
            print("\n\n\nhey you I think it is too low ")
        elif guess > random_number:
            print("\n\nhey you, it is too high from the target")
        else:
            print(f"\n\nhey you got it right the number is {random_number} you are good with this" )

guess(10)

def computer_guess(x):
    print("\n\nNOW IT'S MY TURN TO GUESS")
    low = 1
    high = x
    feedback =''
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low ,high)
        else:
            guess = low
        feedback = input (f" \n\n\n{guess} is correct!!\n # If the number is too high press (H) \n # if too low press (L)\n #c if correct press (C) : ").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1

    print("\n\nhurrayyy I gussed your number smarlty , I can also think like you")
            
computer_guess(10)