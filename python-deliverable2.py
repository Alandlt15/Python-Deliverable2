print("Welcome to GC Fruit Market!")
name = input("What is your name? ")
print()
tab = 0.00
apples = 0
grapes = 0
oranges = 0
yes_no = 'y'

while yes_no == 'y':
    print(f"Welcome {name}. Which fruit would you like to buy?")
    print("1. Apple $2")
    print("2. Grape $1")
    print("3. Orange $3")
    choice = int(input())

    if choice == 1:
        print("You bought 1 Apple at $2")
        tab += 2.00
        apples += 1
    elif choice == 2:
        print("You bought 1 Grape at $1")
        tab += 1.00
        grapes += 1
    elif choice == 3:
        print("You bought 1 Orange at $3")
        tab += 3.00
        oranges += 1

    yes_no = input("Would you like to buy another piece of fruit? y/n ")

print(f"Order for {name}")
print(f"{apples} apple(s) at $2 apiece")
print(f"{grapes} grape(s) at $1 apiece")
print(f"{oranges} orange(s) at $3 apiece")
print(f"Sub Total: ${tab}")
print(f"5% Tax: ${(tab * .01) * tab}")
print(f"Total: ${(tab + (tab * .01) * tab)}")