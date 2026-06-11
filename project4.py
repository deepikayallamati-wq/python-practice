print("Project 4 : Student Record System")
print()
student1 = {"name": "Deepika",
           "age":"19",
           "branch":"IT"}
student2 = {"name":"Sathya",
           "age":"19",
           "branch":"IT"}
student3 = {"name":"Samyuktha",
           "age":"19",
           "branch":"IT"}
students = [student1,student2,student3]
subjects = ("Python","DSA","DBMS")
Python = ["98","97","97"]
DSA = ["95","96","98"]
DBMS = ["99","93","96"]
marks = [Python,DSA,DBMS]
for student in students:
      print("Name:",student["name"])
      print("Age:",student["age"])
      print("Branch:",student["branch"])
      print()
for subject in subjects:
      print("Subject",":",subject)
      print()    
for i in range(3):
      print(subjects[i],":",marks[i])
      print()
      
            
      
       
       
              
      



    
   



