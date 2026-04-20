Operation = input("what operation would u like to do? +, -, *, /:  ")
X = float(input("enter ur first no.:  "))
Y = float(input("enter ur second no.:  "))
if Operation == "+":
    print(X + Y)
elif Operation == "-":
    print(X - Y)
elif Operation == "*":
    print(X * Y)
elif Operation == "/":
    print(X / Y)
else: print("enter a valid operation only!!")
