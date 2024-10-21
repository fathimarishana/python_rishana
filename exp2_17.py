my_dict = {}
n = int(input("enter the number of items in the dictionary:"))
for _ in range(n):
   key = input("enter key:")
   value = int(input("enter value:"))
   my_dict[key] = value
print("sorted by keys(ascending):",dict(sorted(my_dict.items())))
print("sorted by key (descending):",dict(sorted(my_dict.items(),reverse=True)))
print("sorted by values(ascending):",dict(sorted(my_dict.items(),key=lambda item:item[1])))
print("sorted by values(descending):",dict(sorted(my_dict.items(),key=lambda item:item[1],reverse=True)))
