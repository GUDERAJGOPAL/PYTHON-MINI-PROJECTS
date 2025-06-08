import random
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters=['0','1','2','3','4','5','6','7','8','9']

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', 
    '"', "'", '<', '>', ',', '.', '?', '/', '|', '\\', 
    '`', '~'
]
alpha=int(input("enter how many letters you want in passward:"))
letter=int(input("enter how many letters you want in passward:"))
symbol=int(input("enter how many letters you want in passward:"))
password=[]
for i in range(1,alpha+1):
    t=random.choice(alphabets)
    password.append(t)
for i in range(1,letter+1):
    t=random.choice(letters)
    password.append(t)
for i in range(1,symbol+1):
    t=random.choice(symbols)
    password.append(t)
random.shuffle(password)
passwords=""
for i in password:
    passwords+=i
print(passwords)