import random

card=["A",2,3,4,5,6,7,8,9,10,"J","Q","R"]
name=["Spades", "Hearts", "Diamonds", "Clubs"]
print("for smit:")
for i  in range(3):
    x=random.choice(card)
    y=random.choice(name)
    print(str(x)+ " of "+str(y))
print("\nfor darshil:")
for i  in range(3):
    x=random.choice(card)
    y=random.choice(name)
    print(str(x)+ " of "+str(y))
