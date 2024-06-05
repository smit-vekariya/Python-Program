import random

you_choice=False
com_score=0
you_score=0

while True:
    you_choice=int(input("Enter your chice:(1.rock,2.paper,3.scissors)\n"))

  #  while you_choice>3 or you_choice<1:
   #     you_choice=int(input("Enter your chice:(1.rock,2.paper,3.scissors)\n"))
   
    if you_choice==1:
      you='Rock'
    elif you_choice==2:
      you='Paper'
    elif you_choice==3:
      you='Scissor'


    com_choice=random.randint(1,3)
    if com_choice==1:
        com="Rock"
    elif com_choice==2:
        com="Paper"
    elif com_choice==3:
        com="Scissors"

    
    print("Your Result:")
    if com_choice==you_choice:
      print("tie")
    elif you_choice==1:
      if com_choice==2:
          print("you lose.", com, "covers", you)
          com_score+=1
      else:
          print("you win.", com, "smashes", you)
          you_score+=1
    elif you_choice==2:
      if com_choice==3:
          print("you lose.", com, "covers", you)
          com_score+=1
      else:
          print("you win.", com ,"smashes", you)
          you_score+=1
    elif you_choice==3:
      if com_choice==1:
          print("you lose.", com, "covers", you)
          com_score+=1
      else:
          print("you win.", com ,"smashes" ,you)
          you_score+=1

    elif you_choice=="End" or "end":
      print("final score:")
      print(f"compuert score:{com_score}")
      print(f"your score:{you_score}")
      break

     

  


