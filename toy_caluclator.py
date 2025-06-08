import random
def main():
    try:
        n=int(input("Level:"))
        score=0
        c=0
        print(f"Level {n} started\n lets play.....")
        for i in range(10):
            x=get_x(n)
            y=get_y(n)
            res=0
            t=0
            for _ in range(0,3):
                print(f"{x}+{y}=",end="")
                res=int(input())
                if x+y==res:
                    t=1
                    score+=1
                    break
                else:
                    print("EEE")
            if t!=1:
                print(f"{x}+{y}={x+y}") 
                t=0           
        print("Score:",score,"\n Game ended")
    except ValueError:
        main()
def get_x(n):
    if n==1:
        x=random.randint(0,9)
        return x
    if n==2:
        x=random.randint(10,99)
        return x
    if n==3:
        x=random.randint(100,999)
        return x
def get_y(n):
    if n==1:
        y=random.randint(0,9)
        return y
    if n==2:
        y=random.randint(10,99)
        return y
    if n==3:
        y=random.randint(100,999)
        return y
main()

                