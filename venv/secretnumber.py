'''
game finding a secret number within 3 attempts using while loop
'''
import random
random_no = random.randint(1,10)
guess = int(input('enter your guess number: '))
i=1
while i<=3:
    if guess== random_no:
         print(f"Congratulations, your guess is correct!")
         break
    else:
        guess = int(input("guess again: "))
    i+=i
