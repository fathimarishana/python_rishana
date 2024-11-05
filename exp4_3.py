def copare(s1,s2,n):
    if len(s1) <n or len(s2) <n:
        return False
    if s1[:n] == s2[:n]:
        return True
    else:
        return False
def main():
    s1 = input("enter the 1st string(s1):")
    s2 = input("enter the 2nd string(s2):")
    n = int(input("enter the number of characters to copare (n):"))
    result = copare(s1,s2,n)
    if result:
        print(f"the first {n} characters of both strings are the same.")
    else:
        print(f"the first {n} characters of both stringas are different.")
if __name__ == "__main__":
    main()
