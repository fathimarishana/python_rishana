word = input("enter a string:")
if word [-3:] == "ing":
    result = word + 'ly'
else:
    result = word + 'ing'
print("modified string:",result)
