def show_magicians(mag_names):
      print("Here is the name of the magicians")
      print("The old list is :", mag_names)
      for magician in mag_names[:]:
          full_name = mag_names.pop() 
          printed_list.append(full_name.title())
          print("The name of the magician is ", full_name.title())
      print("The old list now :", mag_names)
      print("The new list is :", printed_list)

magicians = ['houdini', 'williams', 'sunderland']
printed_list = []
show_magicians(magicians)   
