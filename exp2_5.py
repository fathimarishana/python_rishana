names = input("enter 1st names seperated by commas:").split(',')
count_a = sum(name .lower().count('a')for name in names)
print(f" the letter 'a' occurs {count_a} times in the list of names")
