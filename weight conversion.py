A = float(input("enter the weight of the object: "))
Unit = input("enter the unit of weight(kg, g, mg, lb, oz):  ")
B = input("enter the unit you want to convert to(kg, g, mg, lb, oz):  ")
if Unit == "kg" and B == "g":
    print(A * 1000)
elif Unit == "kg" and B == "mg":
    print(A * 1000000)
elif Unit == "kg" and B == "lb":
    print(A * 2.20462)
else:
    print("enter a valid unit only!!")