print "Welcome to the Menumanager"

menu = {}

while True:

    dish = raw_input("please enter a dish: ")
    price = raw_input("please enter the price: ")

    menu [dish] = price

    new = raw_input("would you like to add another dish?")

    if new == "no":
        break

menu_file = open("menu.txt", "w+")

print "Daily Menu:"
menu_file.write("Daily Menu:\n")
for i in menu:
    print i + " " + menu [i] + "$"
    menu_file.write(i + " " + menu [i] + "$" + "\n")

menu_file.close()
