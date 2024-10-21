dict1 = {}
n1 = int(input("enter number of items in first dictionary:"))
for _ in range(n1):
    key = input("enter key:")
    value = input("enter values:")
    dict1 [key] = value
dict2 = {}
n2 = int(input("enter number of items in second dictionary:"))
for _ in range(n2):
    key = input("enter key:") 
    value = input("enter values:")
    dict2 [key] = value
merged_dict = {**dict1,**dict2}
print("merged dictionary :",merged_dict)
