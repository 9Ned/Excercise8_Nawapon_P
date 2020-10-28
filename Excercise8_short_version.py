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

        product = ["iMac", "MacBook Pro", "iPhone 12", "iPad pro 12.9 inches"]
        price = [450000, 150000, 55000, 45000]

        while run:
            selected1 = int(input("please select your 1st product(1-4):"))
            if selected1 <= 4:
                item1 = product[selected1-1]
                price1 = price[selected1-1]
                print("You have selected ", item1)
                print("The Price is ", price1)
                amount1 = int(input("Please enter amount:"))
                totalprice1 = price1*amount1
                print("Total Price1 =", totalprice1)
                break
            else:
                print("Please enter 1-4")

        while run:
            selected2 = int(input("please select your 2nd product(1-4):"))
            if selected2 <= 4:
                item2 = product[selected2-1]
                price2 = price[selected2-1]
                print("You have selected ", item2)
                print("The Price is ", price2)
                amount2 = int(input("Please enter amount:"))
                totalprice2 = price2*amount2
                print("Total Price2 =", totalprice2)
                break
            else:
                print("Please enter 1-4")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("Net Price =", (price1+price2)*1.07)
        print("Thank you for shopping with us!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        exit()

    else:
        print("OOPS! Wrong username or password, please try again!")

