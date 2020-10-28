run = True
while run:
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

        while run:
            shoppingList1 = int(input("please select your 1st product(1-4):"))
            if shoppingList1 == 1:
                print("You have selected iMac")
                amount1 = int(input("Please enter amount:"))
                price1 = 450000 * amount1
                print("Prict of iMac =", price1)
                break
            elif shoppingList1 == 2:
                print("You have selected MacBook Pro")
                amount1 = int(input("Please enter amount:"))
                price1 = 150000 * amount1
                print("Prict of MacBook Pro =", price1)
                break
            elif shoppingList1 == 3:
                print("You have selected iPhone 12 ")
                amount1 = int(input("Please enter amount:"))
                price1 = 550000 * amount1
                print("Prict of iPhone 12 =", price1)
                break
            elif shoppingList1 == 4:
                print("You have selected iPad pro 12.9 inches")
                amount1 = int(input("Please enter amount:"))
                price1 = 450000 * amount1
                print("Prict of iPad pro 12.9 inches =", price1)
                break
            else:
                print("Please enter 1-4")
        while run:
            shoppingList2 = int(input("please select your 2nd product(1-4):"))
            if shoppingList2 == 1:
                print("You have selected iMac")
                amount2 = int(input("Please enter amount:"))
                price2 = 450000 * amount2
                print("Prict of iMac =", price2)
                run = False
            elif shoppingList2 == 2:
                print("You have selected MacBook Pro")
                amount2 = int(input("Please enter amount:"))
                price2 = 150000 * amount2
                print("Prict of MacBook Pro =", price2)
                run = False
            elif shoppingList2 == 3:
                print("You have selected iPhone 12 ")
                amount2 = int(input("Please enter amount:"))
                price2 = 550000 * amount2
                print("Prict of iPhone 12 =", price2)
                run = False
            elif shoppingList2 == 4:
                print("You have selected iPad pro 12.9 inches")
                amount2 = int(input("Please enter amount:"))
                price1 = 450000 * amount2
                print("Prict of iPad pro 12.9 inches =", price2)
                run = False
            else:
                print("Please enter 1-4")

        print("Total Price =", (price1+price2)*1.07)
        print("Thank you for shopping with us!")

    else:
        print("OOPS! Wrong username or password, please try again!")


