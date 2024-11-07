def add_numbers():
    user_input = input("enter numbers seperated by space:")
    numbers = [int(num)for num in user_input.split()]
    return sum(numbers)
result = add_numbers()
print(f"the sum of the numbers is:{result}")
