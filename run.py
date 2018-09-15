import random

#def play():
num=0
input("Press Enter to Start the Game\n")
b = random.randint(1,100)
#print("The b=",b)
for i in range(1,(b+1)):
	input("Please press the key")
	n=random.randint(0,6)
	if(n==0):
		print("!!!!You are out!!!")
		break
	elif(n==1):
		print("You scored 1 run")
	elif(n==2):
		print("You scored 2 run")
	elif(n==3):
		print("You scored 3 run")
	elif(n==4):
		print("Bravo you hit a boundry")
	elif(n==5):
		print("You get a boundry in a no ball")
	elif(n==6):
		print("Bravo It's a Sixer")
	num = n+num
print("Your score is", num)

input("Press Ennter to Exit")
