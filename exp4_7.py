n = int(input("enter the number of exponents:"))
exponents = list(range(n))
powers_of_2 = map(lambda x: 2 ** x,exponents)
print(f"power of 2 is :{list(powers_of_2)}")
