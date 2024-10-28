num = int(input("enter a number to find it's factor:"))
i=1
factors = []
while i <= num:
    if num %i == 0:
        factors.append(i)
    i += 1
print(f"the factors of {num} are:{factors}")

