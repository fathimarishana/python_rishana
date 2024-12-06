def validate_voter(name,age):
    if not name.isalpha():
        return"invalid name.please enter alphabetic character only"
    if age<0:
        return "invalid age.age cannot be negative"
    if age>=18:
        return f"{name},you are  eligible to vote."
    else:
        return f"{name}, you are not eligible to vote yet.you need to be at least 18 years old "
name=input("enter your name:").strip()
try:
    age=int(input("enter your age").strip())
    result=validate_voter(name,age)
    print(result)
except valueError:
    print("invalid age.please enter a valid number.")

