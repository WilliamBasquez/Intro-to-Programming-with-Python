import random

def main():
    actual_number = random.randint(1, 20)

    low, high = 1, 20
    tries = 0
    guessed = False

    while guessed != True and tries < 3:
        user_guess = int(input(f"Enter a number from {low} - {high}: "))
        # TODO: Give the use 3 chances to guess a number

        # TODO: Update the variables 'low' and 'high' so that the user knows what range their next guess should be

        # TODO: Don't forget to increase the number of tries, to avoid an infinite loop

    if guessed == True:
        print("You Won!")
    else:
        print("Sorry, the actual number is:", actual_number)


if __name__ == '__main__':
    main()
