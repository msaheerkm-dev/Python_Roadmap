a=int(input("Enter the first number..."))
b=int(input("Enter the second number..."))
calculator ={
    "add":lambda:a+b,
    "subtract":lambda:a-b,
    "multiply":lambda:a*b,
    "divide":lambda:a/b
}
print("enter your choice:")
print(list(calculator.keys()))
choice = input()
if choice in calculator:
    print(calculator[choice]())
else:
    print("Invalid choice")