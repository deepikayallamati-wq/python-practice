
print("Project_3 : Student Login System")
username = "admin"
password = "python123"
attempt = 0 
uname = None
paswod = None
login_succ = False
while not login_succ and attempt <3:
    uname = input("Enter username: ")
    paswod = input("Enter password: ")
    if uname =="" and paswod =="":
         print("Username and Password are empty")
         attempt += 1
    elif uname == "":
         print("username empty")
         attempt += 1
    elif paswod =="":
         print("password empty")
         attempt += 1
    elif uname != username and paswod != password:
         print("Username and password Error")
         attempt += 1
    elif uname != username:
         print("username Error")
         attempt += 1
    elif paswod != password:
         print("password Error")
         attempt += 1
    else: 
        login_succ = True
        print("Succesful Login")
if attempt == 3:
     print("Maximum attempts completed")        


         
          
    
    
    
   
   
               


