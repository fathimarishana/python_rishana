def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact
def sum_series(n):
    series_sum = 0
    for i in range(1, n+1):
        series_sum += (i **i)/factorial(i)
    return series_sum
n = int(input("enter the number of terms (n):"))
result = sum_series(n)
print(f"the sum of the series up to {n} terms is:{result}")
