
words = input("enter words seperated by spaces:").split()
max_length = max(len(word) for word in words)
print("length of the largest word:", max_length)
