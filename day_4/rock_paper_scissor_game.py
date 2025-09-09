import random

print("Welcome to the Rock Paper Scissors Game \n\n")
game_list=["rock","paper","scissors"]
userchoice=input("Enter your choice\n").lower()
botchoice=(random.choice(game_list))

# Userchoice

if userchoice=="rock":
   print(r'''                                  88         
                                  88         
                                  88         
    8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
    88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
    88         8b       d8 8b         8888[      
    88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
    88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a ''')
   print("\nYou Choose :  Rock--- ")

elif userchoice == "paper":
    
    print('''                                                          
    8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
    88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
    88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
    88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
    88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
    88                     88                                 
    88                     88                                 
    ''')
    print("\nYou Choose : Paper -----")

elif userchoice == "scissors":
    
    print('''    ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
    ''')
    print("\nYou Choose : Scissors---")

else:
    print("enter a correct choise")

# Botchoice

if botchoice=="rock":
    print("Bot Choose :  Rock--- ")
    print(r'''                                  88         
                                  88         
                                  88         
    8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
    88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
    88         8b       d8 8b         8888[      
    88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
    88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a ''')

elif botchoice == "paper":
    print("Bot Choose : Paper -----")
    print('''                                                          
    8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  
    88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8  
    88       d8 ,adPPPPP88 88       d8 8PP""""""" 88          
    88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88          
    88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88          
    88                     88                                 
    88                     88                                 
    ''')
else:
    print("Bot Choose : Scissors---")
    print('''    ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
    ''')
# condition
if userchoice==botchoice:
    print("Match Draw") 
elif (userchoice=="rock" and botchoice =="scissors") or (userchoice=="paper" and botchoice =="rock") or (userchoice=="scissors" and botchoice=="paper"):
    print("You Win!")
elif userchoice in game_list:
    print("You Lose")
else:
    print("Enter a correct choice")







