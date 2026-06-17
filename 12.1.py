try:
      numerator = int(input("Enter a number to divide: "))
      denominator = int(input("Enter a number to divided by: "))
      result = numerator/denominator
except ZeroDivisionError as a:
      print(a)
      print("You can't divide by zero")
except ValueError as a:
      print(a)
      print("Enter only numbers")            
except Exception as a:
       print(a)
       print("Something went wrong :(")
else:
      print(result)  
finally:
      print("Program executed")                 