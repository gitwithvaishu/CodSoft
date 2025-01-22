import random as rand
print("Welcome to \"ROCK PAPER SCISSORS\" game...")
user_score=0
comp_score=0
while True:
    print("\nChoices\n1.Rock\n2.Paper\n3.Scissors\n")
    user_choice=int(input("Enter your choice:"))
    comp_choice=rand.randint(1,3)
    if user_choice==1:
        print("Your choice: Rock")
    elif user_choice==2:
        print("Your choice: Paper")
    else:
        print("Your choice: Scissors")
    if comp_choice==1:
        print("Computer choice: Rock ")
    elif comp_choice==2:
        print("Computer choice: Paper")
    else:
        print("Computer choice: Scissors")
    if user_choice==1 and comp_choice==2:
        print("Computer Won")
        comp_score+=1
    elif user_choice==1 and comp_choice==3:
        print("You won")
        user_score+=1
    elif user_choice==2 and comp_choice==1:
        print("You Won")
        user_score+=1
    elif user_choice==2 and comp_choice==3:
        print("Computer won")
        comp_score+=1
    elif user_choice==3 and comp_choice==1:
        print("Computer won")
        comp_score+=1
    elif user_choice==3 and comp_choice==2:
        print("You won")
        user_score+=1
    else:
        print("Its TIE")
        comp_score+=1
        user_score+=1
    print("Your score: ",user_score)
    print("Computerr score: ",comp_score)
    con_choice=input("Do you want to continue(y/n):")
    if con_choice.lower()=='y':
        continue
    else:
        break
