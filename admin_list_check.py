exist = ['sofia','Billy','williams','Philip','bary','peter']
empty = []

for old in exist:
     empty.append(old.lower())

new = ['sofia','billy','tony','Williams','Philip','larry']

for new_user in new:
     if (new_user.lower()) in empty:
          print("You will need to enter a new username")
     else:
          print("Username is available.")
     
