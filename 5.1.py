temp = int(input("what is the temparature outside?: "))
if not(temp >=0 and temp <=32):
    print("The temparature is good today!")
    print("Go outside!")
    print("Enjoy")
elif not(temp <0 or temp >32):
    print("The temperature is bad today!")
    print("stay inside!")