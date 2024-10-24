mylist = list(map(int,input("enter the elements(seperated by space):").split()))
total = 0
for i in range (0,len(mylist)):
   total = total + mylist[i]
print("sum of all elements in given list:",total)
