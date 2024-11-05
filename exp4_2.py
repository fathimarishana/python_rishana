def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
def main():
    num = int(input("enter a number:"))
    result = check_even_odd(num)
    print(f"the number {num} is {result}.")
if __name__ == "__main__":
        main()
