import random

limit = int(input("Enter the upper limit for the range of possible numbers: "))

def run(limit):
    random_num = random.randint(1, limit)
    guess = 0
    count = 0
    while guess != random_num:
        guess = int(input("Enter your guess: "))

        if guess > random_num:
            print("Guess a smaller number")
        elif guess < random_num:
            print("Guess a bigger number")
        else:
            print("Well done! You guessed correctly.")
        count+=1
    print(f"Congratulations for finding the random number generated! The number was {random_num} and you needed {count} tries in order to find it.")
run(limit)