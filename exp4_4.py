def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i),end=" ")
def main():
    n = int(input("enter the number of terms for fibonacci series:"))
    print("fibonacci series:")
    print_fibonacci_series(n)
if __name__ == "__main__":
    main()
