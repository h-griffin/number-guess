#Danny Rigdon - 09/18/2020
#HW05 - Guess the Number / Game

#Declare/initialize variables and CONSTANTS

CORRECT_NUMBER = 35
userGuess = 0
attempts = 0
bounds = (1, 100)
QUESTION_ONE = ""
userAnswerOne = "Yes"
userAnswerTwo = "yes"
userAnswerThree = "YES"
win = False



#Does the user want to guess which number I am thinking of?

QUESTION_ONE = input("I am thinking of a number. Would you like to guess what that number is? (Yes or No) ")
if QUESTION_ONE == userAnswerOne:
    print("Great! Let's get started.")
elif QUESTION_ONE == userAnswerTwo:
    print("A challenger?")
elif QUESTION_ONE == userAnswerThree:
    print("Can't say I believe in you, but let's do this!")
else:
    print("You're no fun!") + quit()
        
#Prompt user for entry / Process user input.

while userGuess != CORRECT_NUMBER:
    userGuess = int(input("Please guess a number between 1 and 100: "))
    attempts += 1
    if userGuess > 100: # 101
        print ("Your guess was not in range... if you want to win, please guess a number between 1 and 100!")
        continue
    if userGuess < 1:
        print ("Your guess was not in range... if you want to win, please guess a number between 1 and 100!")
        continue
        
#Process continued / Display output results.
        
    if userGuess < CORRECT_NUMBER:
        print("That guess is too low... are you trying? Guess again!")
    elif userGuess > CORRECT_NUMBER:
        print("That guess is too high... get your head in the game. Guess again!")
    elif userGuess == CORRECT_NUMBER:
        win = True
        break

#Final Level

if win == True:
    print("Great guess! The number was, in fact, " + str(CORRECT_NUMBER) + ".")
    print("It took you " +str(attempts) + " attempt(s) to guess the correct number.")
if attempts == 1:
    print("Why do I feel like you cheated and looked at the source code? Anyways, good game!")
elif win == False:
    print("You're no match for me. You are out of guesses! You LOSE!")
         
print("THE END :)")