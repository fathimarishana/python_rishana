def calculate_simple_interest(principal,rate,time):
    return (principal*rate*time)/100
def get_customer_details():
    principal = float(input("enter the principal amound:"))
    time = float(input("enter the time(in years):"))
    is_senior_citizen = input("is the customer a senior citizen?(yes/no):").strip().lower()
    if is_senior_citizen == 'yes':
        rate = 12
    else:
        rate = 10
    return principal,rate,time
def main():
    principal,rate,time= get_customer_details()
    interest = calculate_simple_interest(principal,rate,time)
    print(f"the simple interest is :{interest}")
if __name__ == "__main__":
        main()
