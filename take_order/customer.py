print("Welcome to my resturant can i take your order")
print("In our menu we have Chips, Hamburger and Pizza")
order = input("What would you like to order? ")
if order == "Hamburger" or order == "hamburger":
    print("Great choice")
    cheese = input("Would you like some extra cheese? ")
    if  cheese == "yes" or cheese == "Yes":
        print("Hamburger with extra Cheese i got you")
    else:
        print("No extra cheese i got you")
elif order == "Chips" or order == "chips":
    print("Awesome choice quick choice")
    cheese = input("Would you like some Chese sauce in there ? ")
    if cheese == "Yes" or cheese == "yes":
        print("Chips with extra cheese coming up")
    else:
        print("Chips coming up")
elif order == "Pizza" or order == "pizzza":
    print("Grat Pizza coming up")
    paperoni = input("Do you want to add some peperoni? ")
    if paperoni == "yes" or paperoni == "Yes":
        print("Pizza with paperoni coming up")
    else:
        print("Pizza coming up you way")
else:
    print("Please order what we have on the Menu stated")

