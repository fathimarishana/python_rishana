n=int(input("enter the number of step for the pyramid:"))
for i in range (1,n+1):
    row = [str(i*j) for j in range (1,i+1)]
    print(" ".join(row))
