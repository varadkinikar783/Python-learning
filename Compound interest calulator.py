Principal = P = int(input("What is the principal amount?: $"))
Rate = R = float(input("What is the rate of interest on your loan?: "))
Time_period = T = int(input("What is the time period of your loan?: "))
n = int(input("Please enter the no. of times the loan is compounded in an year. "))
Amount = A = P * (1 + ((R / 100) / n)) ** (n * T) 
print(f"The amount you will have to pay is ${A:.2f}")
X = input("Would you like to know the interest you will be paying(Y/N)? ")
if X == "Y" or X == "y" : 
    print(f"The interest is ${A - P:.2f}")
else :
     print("Thank you for using our calculator!")   
print("Thank you for using our services!!") 