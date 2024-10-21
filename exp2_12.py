integer_list=list(map(int,input("enter integers space separated:").split()))
odd_number=[]
for number in integer_list:
    if number % 2 != 0:
        odd_number.append(number)
print("list of odd number",odd_number)
