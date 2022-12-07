import random
 # snake water gun game 
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="s" :
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="w":
            return True
        elif you=="s":
            return False        


print("Comp's turn: Snake(s) Water(w) or Gun(g)")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp="w"    
elif randNo==3:
    comp="g" 

you=input("Your turn: Snake(s) Water(w) or Gun(g)")
a=gamewin(comp,you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("Its a tie")
elif a==True:
    print("You win!")
else:
    print("You Lose!")