Principal = P = float(input("What is the principal amount?: $"))
while P <= 0:
    print("Principal can't be negative")
    P = float(input("Please enter the correct principal: $"))
Rate = R = float(input("What is the rate of interest on your loan?: "))
while R <= 0:
    print("rate can't be negative")
    R = float(input("Please enter the correct rate of interest: "))
Time_period = T = int(input("What is the time period of your loan?: "))
while T <= 0:
    print("Time period of the loan can't be negative")
    T = float(input("Please enter the correct time period of the loan: "))
n = int(input("Please enter the no. of times the loan is compounded in an year. "))
while n <= 0:
    print("Compounding frequency can't be negative")
    n = float(input("Please enter the correct compounding frequency: "))
Amount = A = P * (1 + ((R / 100) / n)) ** (n * T) 
print(f"The amount you will have to pay is ${A:.2f}")
X = input("Would you like to know the interest you will be paying(Y/N)? ")
if X == "Y" or X == "y" : 
    print(f"The interest is ${A - P:.2f}")
else :
     print("Thank you for using our calculator!")   
print("Thank you for using our services!!") 