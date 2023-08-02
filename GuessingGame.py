#Prompt: Create a program in which the user tries to guess a secret number. User has three tries before they fail.

secret_number = 42
attempts = 0
guess = 0
while attempts < 3 and guess != secret_number:
    guess = input("Guess the secret number: ")
    if(int(guess) == secret_number):
        print("You got it! Congrats!")
        break
    else:
        attempts += 1
        print("It's not ", guess, ". You have ", (3 - attempts), " tries left.")