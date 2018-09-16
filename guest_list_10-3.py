print("Please enter the guest name.")
print("Enter 'q' to quit.")

''' Initialisation of the File'''

with open(r'C:\Users\erajmuk\Desktop\PY\guest_list.txt', 'w') as file_object:
    file_object.write("Welcome to the Guest Directory\n")

''' Defination of the tables'''

def guest_entry(rec_guest_name):
    with open(r'C:\Users\erajmuk\Desktop\PY\guest_list.txt', 'a') as file_object:
        file_object.writelines(rec_guest_name +'\n')

def display_names():
    with open(r'C:\Users\erajmuk\Desktop\PY\guest_list.txt', 'r') as file_object:
        guest_names = file_object.readlines()
        for name in guest_names:
            print(name.strip().title())

''' Main program starts from Here'''

while 1:
    guest_name = input('Type your name here :  ')
    if guest_name != 'q':
        print("Welcome Mr/Ms " + guest_name.title() + ' to the Hotel')
        guest_entry(guest_name)
    else:
        break
                
print("\nHere goes the Name of the Guest's in the Hotel :")
display_names()
