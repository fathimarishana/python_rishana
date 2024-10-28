num=int(input("enter a number to reverse:"))
reverse_num=0
original_num=num
while num>0:
    digit = num %10
    reverse_num= reverse_num*10 + digit
    num //=10
print (f" the reverse of {original_num} is:{reverse_num}")
