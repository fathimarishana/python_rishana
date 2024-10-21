integers = list(map(int,input("enter a list of integers (space seperated):").split()))
N = int(input("enter a number N:"))
word = input("enter a word:")
positive_numbers = [x for x in integers if x>0]
squared_numbers = [x**2 for x in range(N)]
vowels = [char for char in word if char in 'aeiouAEIOU']
ordinal_values = [ord(char)for char in word]
print("+ve number:",positive_numbers)
print("squared numbers:",squared_numbers)
print("vowels:",vowels)
print("ordinal values:",ordinal_values)
