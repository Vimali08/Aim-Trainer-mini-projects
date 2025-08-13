print("Welcome to the quiz game!")
playing=input("Do you want to play? (yes/no) ")
if playing.lower() != "yes":
    quit()
print("Okay Let begin!")
score=0

ans1=input("What is the name of India's prime minister? ")
if ans1.lower() == "narendra modi":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

ans2= input("What is the capital of Japan? ")
if ans2.lower() == "tokyo":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

ans3=input("What is the name of America's president? ")
if ans3.lower()=="donald trump":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

ans4=input("What is India's capital? ")
if ans4.lower()=="new delhi":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

ans5=input("What is the process of making food in plants is called? ")
if ans5.lower()=="photosynthesis":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

print(f"You got {score} questions correct!")
percent=(score/5)*100
print(f"You got {percent} in total")

