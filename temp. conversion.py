X = float(input("enter the temp. u wish to convert: "))
U = input("enter the unit of the temp. u wish to convert: ")
Y = input("enter the unit to which u wish to convert the given temp. to: ")
if U =="C/c" and Y =="F/f":
    print((X * 9/5) + 32)
elif U =="C/c" and Y == "K/k":
    print(X + 273)
elif U =="F/f" and Y == "C/c":
    print((X - 32) * 5/9)
elif U =="F/f" and Y == "K/k":
    print((X - 32) * 5/9 + 273)
elif U =="K/k" and Y == "C/c":
    print(X - 273)
elif U =="K/k" and Y == "F/f":
    print((X - 273) * 9/5 + 32)
elif U == "C/c" and Y == "C/c":
    print(X)
elif U == "F/f" and Y == "F/f":
    print(X)
elif U == "K/k" and Y == "K/k":
    print(X)
else: print("enter a valid unit only!!")
# here 'and' is a logical operator about which u will learn in the next chapter. It is used to combine two or more conditions and returns true if all the conditions are true. In this case, it is used to check if both the unit of the temp. and the unit to which u wish to convert are valid.