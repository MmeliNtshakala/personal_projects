print("Welcome to my resturant can i take your order")
print("In our menu we have Chips, Hamburger and Pizza")
order = input("What would you like to order? ")
if order == "Hamburger" or "hamburger":
    print("Great choice")
    cheese = input("Would you like some extra cheese? ")
    if  cheese == "yes" or "Yes":
        print("Hamburger with extra Cheese i got you")
    else:
        print("No extra cheese i got you")
elif order == "Chips" or "chips":
    print("Awesome choice quick choice")
    cheese = input("Would you like some Chese sauce in there ? ")
    if cheese == "Yes" or "yes":
        print("Chips with extra cheese coming up")
    else:
        print("Chips coming up")
elif order == "Pizza" or "pizzza":
    print("Grat Pizza coming up")
    paperoni = input("Do you want to add some peperoni? ")
    if paperoni == "yes" or "Yes":
        print("Pizza with paperoni coming up")
    else:
        print("Pizza coming up you way")
else:
    print("Please order what we have on the Menu stated")

