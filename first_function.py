def show_magicians(magicians):
     print("Here is the name of the magicians")
     print(magicians)
     for magician in magicians:
          full_name = magicians.pop()
          print("The name of the magician is ",full_name.title())
          return 0

magicians = ['abs','williams','sunderland']

show_magicians(magicians)
