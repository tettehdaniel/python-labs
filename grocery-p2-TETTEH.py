'''
    Project: Grocery Store Simulator
    Name: Daniel Tetteh
    Date: 02/19/2026
    Course: CSMC 150
    Program Description: A grocery store simulation program
'''

INVENTORY = {"pizza":15, "sparkling water":1.50, "lollipop":0.25, "eggs":3.50,
    # WRITE YOUR 10 GROCERY PRICES HERE #
"steak":15, "burger":5, "crackers":2.50, "bananas":1.5, "jam":2, "orange juice":3}

# -----  CHECKOUT FUNCTIONS  ----- #
# WRITE YOUR CODE BELOW #

receipt = {}

def clerk_checkout():

    ''' This function rings up a food item the user input one at the time and
shows the subtotal after each item is rung. A receipt is shown when the user ends cart'''

# While loop help: Austin Loving (friend)
    subtotal = 0
    
    while True:
        user_item = input("> ")

        # The code below checks if the user's input (user_item) is in the receipt dictionary. If not, it assigns it to the dictionary.

        if user_item in INVENTORY.keys() and user_item not in receipt.keys():
            receipt[user_item] = 1
            subtotal += INVENTORY[user_item]
            print(f"Subtotal: {subtotal:.2f}")

        # From now on the program stores how many times a user inputs a food item and prints a subtotal after every entered item.
        
        elif user_item in INVENTORY.keys():
            receipt[user_item] += 1
            subtotal += INVENTORY[user_item]
            print(f"Subtotal: {subtotal:.2f}")

        # If a user inputs "END CART", the program breaks and prints a receipt featuring the food items, the number of times they appear and unit price

        elif user_item.upper() == "END CART":
            print("\n==== RECEIPT ====")
            for k,v in receipt.items():
                if v != 0:
                    print(f"{k}    {v}    ${INVENTORY[k]:.2f}")
            print(f"TOTAL: ${subtotal:.2f}")
            print("=================\n")
        if user_item.upper() == "END CART":
            break
    
    return


def express_checkout():

    ''' This function rings up food items the user input all at once and
shows the total in a receipt '''

# For loop help: Austin Loving (friend)

    subtotal = 0

    user_item2 = input("> ")

    grocery_list = user_item2.split(",")

    counter = 0

    for item in grocery_list:

        if counter < 10:

            # The code below checks if the user's input (item) is in the receipt dictionary. If not, it assigns it to the dictionary.

            if item in INVENTORY.keys() and item not in receipt.keys():
                receipt[item] = 1
                subtotal += INVENTORY[item]
                
            # From now on the program stores how many times a user inputs a food item and keeps a subtotal of every entered item
            
            elif item in INVENTORY.keys():
                receipt[item] += 1
                subtotal += INVENTORY[item]

        counter += 1

            # A receipt is printed when the user submits their input
    
    print("\n==== RECEIPT ====")
    for k,v in receipt.items():
        if v != 0:
            print(f"{k}    {v}    ${INVENTORY[k]:.2f}")
    print(f"TOTAL: ${subtotal:.2f}")
    print("=================\n")
    return

# MAIN CODE

''' This function asks a user to select which form of checkout they would
like to use and calls that checkout '''

def main():
    user_in = input("Which method would you like to checkout with? [clerk or express]: ")

    if user_in == "clerk":
        clerk_checkout()
    elif "express" in user_in:
        express_checkout()
    else:
        print("That's not an option. Try again")



# calls the main function
if __name__ == "__main__":
    main()
