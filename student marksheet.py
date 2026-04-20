Name = str(input("Enter student name: "))
print("enter the marks aquired in the following subjects:-")
Maths = float(input("Enter the marks aquired in Maths: "))
if Maths < 0 or Maths > 100:
    print("Invalid input. Marks should be between 0 and 100.")
    float(input("Enter the marks aquired in Maths: "))
else:
    M = round((Maths / 100) * 100, 2)
    print(f"you have gotten {M}% in Maths")
Science = float(input("Enter the marks aquired in Science: "))
if Science < 0 or Science > 100:
    print("Invalid input. Marks should be between 0 and 100.")
    Science = float(input("Enter the marks aquired in Science: "))
else:
    S = round((Science / 100) * 100, 2)
    print(f"you have gotten {S}% in Science")
English = float(input("Enter the marks aquired in English: "))
if English < 0 or English > 100:
    print("Invalid input. Marks should be between 0 and 100.")
    English = float(input("Enter the marks aquired in English: "))
else:
    E = round((English / 100) * 100, 2)
    print(f"you have gotten {E}% in English")
Humanities = float(input("Enter the marks aquired in Humanities: "))
if Humanities < 0 or Humanities > 100:
    print("Invalid input. Marks should be between 0 and 100.")
    Humanities = float(input("Enter the marks aquired in Humanities: "))
else:
    H = round((Humanities / 100) * 100, 2)
    print(f"you have gotten {H}% in Humanities")
Biology = float(input("Enter the marks aquired in Biology: "))
if Biology < 0 or Biology > 100:
    print("Invalid input. Marks should be between 0 and 100.")
    Biology = float(input("Enter the marks aquired in Biology: "))
else:
    B = round((Biology / 100) * 100, 2)
    print(f"you have gotten {B}% in Biology")
print(f"you have got a total of { Maths + Science + English + Humanities + Biology} marks out of total 500")
X = Maths + Science + English + Humanities + Biology
Y = round((X / 500) * 100, 2)
print(f" you have scored{Y}% in total")
if Y >= 65:
    print("Congratulations! You have passed the exam.")
else : 
    print("Sorry, you have failed the exam. Better luck next time!")
K = (M < 65 or S < 65 or E < 65 or H < 65 or B < 65)
if K == True:
    print("you have failed in one or more subjects")