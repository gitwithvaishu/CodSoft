import random as rand
def playgame(user_choice,comp_choice):
    
    if user_choice==1 and comp_choice==2:
        print("Computer Won")
        #comp_score+=1
    elif user_choice==1 and comp_choice==3:
        print("You won")
        #user_score+=1
    elif user_choice==2 and comp_choice==1:
        print("You Won")
        #user_score+=1
    elif user_choice==2 and comp_choice==3:
        print("Computer won")
        #comp_score+=1
    elif user_choice==3 and comp_choice==1:
        print("Computer won")
        #comp_score+=1
    elif user_choice==3 and comp_choice==2:
        print("You won")
        #user_score+=1
    else:
        print("  DRAW  ")
       # comp_score+=1
        #user_score+=1
    #print("Your score: ",user_score)
    #print("Computerr score: ",comp_score)
    """con_choice=input("Do you want to continue(y/n):")
    if con_choice.lower()=='y':
       return playgame(user_choice,comp_choice,comp_score,user_score)
    else:
       exit()"""
    
    
print("Welcom to \"ROCK PAPER SCISSORS\" game...")

while True:
    #user_score=0
    #comp_score=0
    print("\nChoices\n1.Rock\n2.Paper\n3.Scissors\n")
    user_choice=int(input("Enter your choice:"))
    comp_choice=rand.randint(1,3)
    match user_choice:
        case 1:
          print("Your choice: Rock")
        case 2:
          print("Your choice: Paper")
        case 3:
          print("Your choice: Scisssors")
    match comp_choice:
        case 1:
          print("Computer choice: Rock")
        case 2:
          print("Computer choice: Paper")
        case 3:
          print("Computer choice: Scissors")
    playgame(user_choice,comp_choice)
    con_choice=input("Do you want to continue(y/n):")
    if con_choice.lower()=='y':
       continue
    else:
        break 
