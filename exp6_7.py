def main():
   try:
        number = float(input("enter a number:"))
        if number >= 0:
            print(f"the number is:{number}")
        else:
            raise ValueError("the entered number is negative.")
   except ValueError as e:
    print(f"Error: {e}")
if __name__ == "__main__":
    main()
~              
