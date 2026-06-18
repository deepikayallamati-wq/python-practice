try:  
      with open("project5.py") as file:
        print(file.read())
except FileNotFoundError:
    print("That File is not found")        
           