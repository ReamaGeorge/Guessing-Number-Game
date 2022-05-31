#NUMBER GUESSING GAME

#store the number

targetNumber = 27

#take user input
print("""This is a Number Guessing Game.
You can win N10,000.
Just pick any number between 20 to 29.""")
userGuess = input("Enter your guess: ")
# Tuserguess = type(userGuess) #str this line is not neccessary

# print(type(userGuess)) #this line also not needed

# Tuserguess is a string and has to be converted to integer.
userGuess = int(userGuess)
# print(type(userGuess))

#We have succefully converted the userGuess from a string to an interger
#Next step is to check if the user's number is same as yours

if userGuess < targetNumber:
    print("Sorry! Your guess is lower, Try a little higher.")
if userGuess > targetNumber:
    print("Sorry! Your guess is higher Try a little lower.")
if userGuess == targetNumber:
    print("Well done! You guessed correctlty. Our secret number is: " + str(targetNumber))

# A while loop is what is required to keep the user repeating the task until the user gets it.
