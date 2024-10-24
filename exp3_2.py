limit = int(input("enter the limit:"))
f,s =0,1
print(f,s)
for i in range (3,limit+1):
  ans = f+s
  print(ans)
  f=s
  s=ans
