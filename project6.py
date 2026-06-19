import random
print("Project_6 : Lucky Number Game with Score History")
print("Welcome")
print("1 : Play_Game ")
print("2 : View_History")
try: 
     choice = input("Enter Choice : ")
     if choice == "1":      
      gnum = int(input("Guess a number from 1 to 9: "))          
      x = random.randint(1,10)
      print("Computer number:",x)
      if x == gnum:  
           print("You Won!") 
           result = "Won"
      else:
           print("Better Luck Next Time")
           result ="Lost"
      text = f"\nGuess:{gnum}, Computer:{x}, Result:{result}\n"
      with open("2_View_History.txt","a") as file:
            file.write(text)       
except ValueError as e:
     print(e)     
     print("Enter only Numbers")
except Exception as e:
     print(e)
     print("Something went wrong")                             
try:             
 if choice == "2":
  with open("2_View_History.txt","r") as file:
                 print(file.read())
except FileNotFoundError:
      print("That File is not found")
             
            

    
