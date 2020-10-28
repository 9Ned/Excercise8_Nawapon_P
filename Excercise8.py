user = input("username:")
pwd = input("password:")
if user =="admin" and pwd =="111":
    print("Access granted")
    print("Welcome to Shop")
    print("---------------")
    print("List of product")
    print("1.iMac                   price 450,000")
    print("2.MacBook Pro            price 150,000")
    print("3.iPhone 12              price 55,000")
    print("4.iPad pro 12.9 inches   price 45,000")
    shoppingList1 = int(input("please select your 1st product:"))
    amount1 = int(input("please select your amount for 1st product:"))
    if shoppingList1 == 1:
        price1 = 450000 * amount1
    elif shoppingList1 == 2:
        price1 = 150000 * amount1
    elif shoppingList1 == 3:
        price1 = 550000 * amount1
    elif shoppingList1 == 4:
        price1 = 450000 * amount1
    else:
        print("please enter 1-4")

    shoppingList2 = int(input("please select your 2nd product:"))
    amount2 = int(input("please select your amount for 2nd product:"))
    if shoppingList2 == 1:
        price2 = 450000 * amount2
    elif shoppingList2 == 2:
        price2 = 150000 * amount2
    elif shoppingList2 == 3:
        price2 = 550000 * amount2
    elif shoppingList2 == 4:
        price2 = 450000 * amount2
    else:
        print("please enter 1-4")

    print("Total price(excluded VAT) =", price1 + price2)
    print("Total price(included VAT) =", (price1 + price2)*1.07)
else:
    print("OOPS! Wrong username or password, please try again!")

