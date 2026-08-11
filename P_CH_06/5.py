#Write a program which finds out whether a given name is present in a list or not.
names = ["Harish", "Rahul", "Ravi", "Arun", "Kiran"]

name = input("Enter a name: ")

if name in names:
    print("Name is present in the list.")
else:
    print("Name is not present in the list.")