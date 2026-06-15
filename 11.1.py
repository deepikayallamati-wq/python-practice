import random
x = random.randint(1,10)
y = random.random()
mylist = ["inky","pinky","ponky"]
z = random.choice(mylist)
cards = [1,2,3,4,5,6,7,8,9,"K","Q","J"]
random.shuffle(cards)
print(x)
print(y)
print(z)
print(cards)