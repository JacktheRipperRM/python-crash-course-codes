print("Print your List")
a = [int(x) for x in input().split(' ')]
print(a)
for i in a:
     if(i>1):
          for s in range(2,i):
               if(i%s)==0:
                    print("Not a Prime Number")
                    break
               else:
                    print("Prime number")
                    break

     
