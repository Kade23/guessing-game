# This is a guessing the number game.
import random

# User's name
print('Hello! What is your name? ')
myName = input()
print("Hi " + str(myName) + "!" + " Let's play a guessing game.")


def random_game():

    play = True
    while play:

        easy = random.randint(1, 10)
        medium = random.randint(1, 20)
        hard = random.randint(1, 50)
        # ask the user to select a difficulty to play on
        print("Would you like to play on easy, medium, or hard? : ")

        level_select = True
        while level_select:
            level = input()
            if level == "easy":
                print("\nAwesome! We'll begin with easy!")
                level_select = not True
                break
            if level == "medium":
                print("\nAwesome! We'll begin with medium!")
                level_select = not True
                break
            if level == "hard":
                print("\nAwesome! We'll begin with hard!")
                level_select = not True
                break
            else:
                print("Invalid input!\nPlease enter either easy, medium or hard. ")


    # If the user selects e for Easy - 20 tries
        if level == 'easy':
            print("On easy mode, you'll have 6 guesses to guess a number between\n1-10.")
            guesses_left = 6
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == easy:
                    print("That's it, you got it right! " + str(easy))
                    print("Congratulations " + str(myName) + "!")
                    break
                elif try1 < easy:
                    print("Nope, Guess higher!")
                elif try1 > easy:
                    print("Nope, Guess lower!")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                # If the user runs out of guesses
                if guesses_left == 0:
                    print('Game Over!')

    # If the user selects m for Medium - 10 tries
        if level == 'medium':
            print("On MEDIUM mode, you'll have 4 guesses to guess a number\nbetween 1-20.")
            guesses_left = 4
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == medium:
                    print("That's it, you got it! " + str(medium))
                    print("Congratulations " + str(myName) + "!")
                    break
                elif try1 < medium:
                    print("Nope, not quite! Guess higher!")
                elif try1 > medium:
                    print("Nope, you're a little high. Guess lower!")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                # If the user runs out of guesses
                if guesses_left == 0:
                    print('Game Over!')

    # If the user selects h for Hard - 3 tries
        if level == 'hard':
            print("On HARD mode, you'll have 3 guesses to guess a number\nbetween 1-100.")
            guesses_left = 3
            while guesses_left != 0:
                try1 = int(input("So, what's your guess? \n"))
                if try1 == hard:
                    print("That's it, you got it right! " + str(hard))
                    print("Congratulations " + str(myName) + "!")
                    break
                elif try1 < hard:
                    print("Nope, not quite! Guess higher!")
                elif try1 > hard:
                    print("Nope, you're a little high. Guess lower!")
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                # If the user runs out of guesses
                if guesses_left == 0:
                    print('Game Over!')

        maybe_play = True
        while maybe_play:
            again = input("\nWould you care to play again?\nYes or No\n ")
            if again == 'No' or again == 'no':
                print('\nOk, Thank you for playing.\nCome back any time!')
                maybe_play = not True
                play = not True
            elif again == 'yes' or again == 'Yes':
                print("\nCool, let's play again!\n")
                maybe_play = not True
                play = True
            else:
                print('Please enter either yes or no.')
                input()
                maybe_play = not True
                play = not True


random_game()
