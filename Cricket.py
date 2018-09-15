import random

num=0
totrun=0
players = []
netrun=0

k = int(input("Press Enter to Number of players : "))

for l in range(1,(k+1)):
        player = input("Enter Name of the Player : ")
        players.append(player)

for player in players:
        b = random.randint(1,100)
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
                        print("Bravo !!!! you hit a boundry")
                elif(n==5):
                        print("You get a boundry in a no ball")
                elif(n==6):
                        print("Bravo !!!! It's a Sixer")
                num = n+num
        print("\n\t", player.title(),"scored :", num,'Run \n\t')
        totrun = totrun+num
netrun=totrun+netrun

print('Your Total score is \n ************* \n ***** %d **** \n *************'%(netrun))
input("Press Enter to Exit")
