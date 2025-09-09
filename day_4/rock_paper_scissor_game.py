import random

print("\n\nWelcome to the Rock Paper Scissors Game \n\n")
game_list=["rock","paper","scissors"]
userchoice=input("Enter your choice\n").lower()
botchoice=(random.choice(game_list))

if userchoice not in game_list:
    print("Enter a correct choice")
    quit()

rock= '''                                 88         
                                88         
                                  88         
    8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
    88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
    88         8b       d8 8b         8888[      
    88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
    88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a    '''

paper='''
    8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
    88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
    88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
    88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
    88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
    88                     88                                 
    88                     88                                   '''

scissors='''    ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/  '''

# Userchoice

if userchoice=="rock":
    print(f"\nYou Choose Rock :\n  {rock}")

elif userchoice == "paper":
    
   print(f"\nYou Choose Paper :\n  {paper}")

else:    
    print(f"\nYou Choose Scissors :\n  {scissors}")


# Botchoice

if botchoice=="rock":
    print(f"\nBot Choose Rock :\n  {rock}")

elif botchoice == "paper":
    
    print(f"\nBot Choose Paper :\n  {paper}")
else:
    print(f"\nBot Choose Scissors :\n  {scissors}")
# condition
if userchoice==botchoice:
    print("Match Draw") 
elif (userchoice=="rock" and botchoice =="scissors") or (userchoice=="paper" and botchoice =="rock") or (userchoice=="scissors" and botchoice=="paper"):
    print("You Win!")
else:
    print("You Lose")







