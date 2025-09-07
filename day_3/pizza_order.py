print("Welcome to pizza deliveries\n")
print(" the menu of our shop is: \n Pizza(S)=100 \n Pizza(M)=150 \n Pizza(L)=200 \n pepperoni=10 or 20 or 30 \n Extra cheese=50\n" )
size= input("what size of pizza do u want? S,M or L\n")
pepperoni = input("Do you want pepperoni on your pizza? Y ot N\n")
extra_cheese = input("Do you want extra cheese on ur pizza? Y or N\n")
bill =0

if size =="S":
    bill= bill+100
    if pepperoni=="Y":
        bill=bill+10
        
            

elif size =="M":
    bill= bill+150
    if pepperoni=="Y":
        bill=bill+20
       


else:
    bill= bill+200
    if pepperoni=="Y":
        bill=bill+30

if extra_cheese =="Y":
            bill=bill+50
        

print(f"the final bill is: {bill}")






 