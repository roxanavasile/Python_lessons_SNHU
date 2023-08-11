#get user input
total = int(input())

#validate user input and perform calculations
if total == 0:
    print("No change")
else:
    money = [
        (100, "Dollar", "Dollars"), 
        (25, "Quarter", "Quarters"), 
        (10, "Dime", "Dimes"), 
        (5, "Nickel", "Nickels"), 
        (1, "Penny", "Pennies")
        ]
    
    for m in money:
        coins = total // m[0]
        total = total % m[0]

        if coins > 1:
            print(f"{coins} {m[2]}")
        elif coins == 1:
            print(f"1 {m[1]}")