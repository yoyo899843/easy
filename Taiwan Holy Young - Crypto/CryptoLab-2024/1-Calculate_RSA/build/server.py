#!/usr/bin/env python3
import random
from time import sleep

FLAG = open('./flag', 'rb').read()

def main():
    seed = random.getrandbits(64)
    random.seed(seed)

    print("you are a mind reader I guess ?")
    print("I will I'll randomly pick 39 numbers. ")
    print("You need to predict the next number Im think about")

    for i in range(39):
        num = random.getrandbits(512)
        print(f"{i+1} = {num}")
    
    next_num = random.getrandbits(512)
    
    print("\nNow, what's my next number?")
    try:
        guess = int(input("Your guess: "))
        if guess == next_num:
            print("Congratulations! Here's your flag:")
            print(FLAG.decode())
        else:
            print("Sorry, that's not correct!")
            print(f"The correct number was: {next_num}")
    except:
        print("Invalid input!")

if __name__ == "__main__":
    main()