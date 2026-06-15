print("Project_5 : Student Result Calculator")
print()
name = (input("Enter Student Name : "))
mark1 = int(input("Enter Subject 1 Marks : "))
mark2 = int(input("Enter Subject 2 Marks : "))
mark3 = int(input("Enter Subject 3 Marks : "))
mark = [mark1,mark2,mark3]
def calculate_total(mark):
    return mark[0] + mark[1] + mark[2]
total = calculate_total(mark) 
print("Total:",total)
def calculate_average(total):
    return total/3
average = calculate_average(total)
print("Average:",average) 
def calculate_grade(average):
         if average >= 90:
                return("A+")
         elif  average >= 80:
                return("A") 
         elif average >= 70:
                return("B")
         elif average  >= 60:
                return("c")
         else:
                return("Fail")
grade = calculate_grade(average)
print("Grade:",grade)         
                 
             
