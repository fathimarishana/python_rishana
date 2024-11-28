from armstrong import is_armstrong
def generate_armstrong_numbers(start,end):
    armstrong_numbers = []
    for number in range(start,end +1):
        if is_armstrong(number):armstrong_numbers.append(number)
    return armstrong_numbers
start = int(input("enter the start of the range:"))
end = int(input("enter the end of the range:"))
armstrong_numbers = generate_armstrong_numbers(start,end)
print("armstrong numbers between", start,"and",end,"are",armstrong_numbers)
    

