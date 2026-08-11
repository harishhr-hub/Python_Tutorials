#Write a program to find the greatest of four numbers entered by the user.
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))
d = int(input("enter d:"))
if(a>b and a>c and a>d):
  print(f"{a} is greater")
elif(b>a and b>c and b>d):
  print(f"{b} is greater")
elif(c>a and c>b and c>d):
  print(f"{c} is greater")
elif(d>a and d>b and d>c):
  print(f"{d} is greater")