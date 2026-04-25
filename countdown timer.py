import time
X = int(input("For how many seconds would you like to set the timer for?: "))
while X <= 0:
    print("Time can't be negative.")
    X = int(input("For how many seconds would you like to set the timer for?: "))
else: 
    for x in range(X, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) 
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
print("time")
