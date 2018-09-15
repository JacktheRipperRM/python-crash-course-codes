users = ['Eric','Admin','Cary','Button','Williams']

for user in users:
	if(user.lower()== 'admin'):
		print("Welcome admin,how do you feel today")
	else:
		print("Thanks for logging in",user.upper())
