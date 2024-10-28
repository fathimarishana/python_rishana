num = int(input("enter a number to check if it's an armstrong number:"))
original_num = num
sum_of_powers =0
num_digits = len(str(num))
while num>0:
    digit = num % 10
    sum_of_powers += digit**num_digits
    num //= 10
if sum_of_powers == original_num:
    print(f"{original_num} is an armstong number")
else:
    print(f"{original_num}is not an armstong number")

