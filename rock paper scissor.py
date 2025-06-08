import random
def Input():
    print("0.Rock\n1.paper\n2.scissor")
    try:
        n=int(input("You:"))
        if n<0 or n>2:
            Input()
        else:
            Start(n)
    except ValueError:
        print("invalid value")
        Input()
def Start(n):
    computer_choice=random.randint(0,2)
    list=["rock","paper","Scissor"]
    if n==computer_choice:
        print("computer choice:",list[computer_choice])
        print("Game Draw")
    elif n>computer_choice:
        print("computer choice:",list[computer_choice])
        print("You Win the game")
    elif n<computer_choice:
        print("computer choice:",list[computer_choice])
        print("Computer win the game")
    elif n==0 and computer_choice==2:
        print("computer choice:",list[computer_choice])
        print("You win the game")
    elif n==2 and computer_choice==0:
        print("computer choice:",list[computer_choice])
        print("Computer win the game")
Input()   
