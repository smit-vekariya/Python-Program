win=20
c=9
# u=int(input("Enter the number:"))

while True:
    c-=1
    if u>win and c!=0:
        print("try lesser.")
        u=int(input("Enter number:"))

    elif u<win and c!=0:
        print("try hgher:")
        u=int(input("Enter number:"))

    elif u==win:
        print("con! you win")
        print("attemp left:",c)
        print("attemp use:",9-c)
        break

    else:
        print("game over")
        break

