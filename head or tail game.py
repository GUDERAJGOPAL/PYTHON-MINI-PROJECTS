import random
try:
    print("enter your choice\n1.Head\n2.tail")
    
    n=input().lower()
    list1=['head','tail']
    result=random.choice(list1)
    #typeerror:random.choice('tail','Head')
    #coorection:random.choice(['tail','head'])
except (ValueError,EOFError,TypeError) as e:
    print(e)
else:
    if n==result:
        print("Result:",result)
        print("You Win game")
    else:
        print("Result:",result)
        print("You Loss the game")  