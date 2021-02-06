tickets = int(input("How many tickets do you require? "))
price = 0

for i in range(tickets):
    age = int(input("How old is the visitor with that ticket? "))
    print()
    if age < 18:
        print("The ticket is free.")
        print()
    elif 18 <= age < 25:
        print("The ticket costs 990 RUB.")
        print()
        price += 990
    elif age >= 25:
        print("The ticket costs 1390 RUB.")
        print()
        price += 1390
print("You need to pay", price, "RUB.")

if tickets >= 3 and price != 0:
    discount = int(price - (price * 0.1))
    print("Your sum with discount is:", discount, "RUB")
