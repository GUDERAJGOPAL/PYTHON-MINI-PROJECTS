def main():
    curr_Balance=1000
    c=0
    print("Welcome to atm simulator")
    print("Please insert your card!!!")
    while True:
        try:
            pin=int(input("Please Enter your pin"))

            if pin==1234:
                break
            else:
                c=c+1
            

            if c==3:
                print("You have completed your chance!!!please try after 24hours\nor consult your bank")
                break
        except:
            print("Please the number should be integer only")
    if c!=3:
        print("Please choose one our service")
        choice=int(input("1.Withdrawl\n2.Depoist\n3.Check_Balance"))
        if choice==1:
            amount=int(input("Enter the amount you want to withdrawl"))
            if amount>curr_Balance:
                print("Insufficient balance")
            else:
                print("Please collect your amount")
                curr_Balance=curr_Balance-amount
        elif choice==2:
            D_Amount=int(input("Please Enter the amount you want to deposit"))
            curr_Balance=curr_Balance+D_Amount
            print("Amount Successfully Deposited")
        elif choice==3:
            print("The current Balance :",curr_Balance)
main()
        
