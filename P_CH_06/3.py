#A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
comment = input("Enter your comment: ")

if ("make a lot of money" in comment.lower() or
    "buy now" in comment.lower() or
    "subscribe this" in comment.lower() or
    "click this" in comment.lower()):
    
    print("This is a Spam Comment")
else:
    print("This is not a Spam Comment")