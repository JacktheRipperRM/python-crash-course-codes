prompt = "\nWelcome to the PVR Cinemas"
prompt+= "\nPlease tell your age :"

age = int(input(prompt))
flag = True
while(flag==True):
     if(age<4):
          print("Free Entry")
          flag = False
          continue
     elif((age>3)&(age<13)):
          print("10$ Entry")
          flag = False
          continue
     else:
          print("15$ Entry")
          flag = False
          continue
     
     
