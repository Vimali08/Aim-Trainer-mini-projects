import random
top_of_range=input("Type a number: ")
guesses=0

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please enter a digit bigger than 0")
        quit()
else:
    quit()
random_number=random.randint(0,top_of_range)

while True:
    guesses+=1
    user_guess=input("Make a guess ")
    if user_guess.isdigit():
        user_guess=int(user_guess)

    else:
        print("Please type a number greater than 0")
        continue

    if user_guess == random_number:
        print("Hooray! you got it right!")
        break
    
    elif user_guess > random_number:
        print("Your guessed number is above the random number")
        
    else:
        print("Your guessed number is below the random number")

print(f"You got it in {guesses} guesses")