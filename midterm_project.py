# Jian Cui
# Midterm project - Display a menu for food court, handle the order and display recipt.

# Constant values
LENGTH_OF_STAR = 47
MENU_LIST = [
    ("De Anza Burger", 5.25),
    ("Bacon Cheese", 5.75),
    ("Mushroom Swiss", 5.95),
    ("Western Burger", 5.95),
    ("Don Cali Burger", 5.95)
]
EXIT_CODE = len(MENU_LIST) + 1
QUANTITY_LIST = [0] * len(MENU_LIST)
ERR_MSG = "Your input is incorrect, please enter again!"
STUDENT_CODE = 0
STUFF_CODE = 1
TAX_RATE = 0.09

# main function
def main():
    show_menu()
    isStudent = get_inputs()
    totalBeforeTax, tax = compute_bill(isStudent)
    print_bill(totalBeforeTax, tax)

# function to show the menu
def show_menu():
    print("*" * LENGTH_OF_STAR)
    print("* Welcome to the food court, here is the menu *")
    counter = 1
    for item, price in MENU_LIST:
        print(f"* {counter}:{item.ljust(30)}{str(price).ljust(12)}*")
        counter = counter + 1

    print("*" * LENGTH_OF_STAR)
# function to get user inputs
def get_inputs():
    finished = False
    totalQuantities = 0
    while not finished:
        selection = ask_selection()
        if selection == EXIT_CODE:
            if totalQuantities == 0:
                print("Thank you! Hope to see you again!")
                exit()
            else:
                finished = True
        else:
            quantity = ask_quantity(selection)
            totalQuantities = totalQuantities + quantity
            QUANTITY_LIST[selection-1] = QUANTITY_LIST[selection-1] + quantity
    #print(QUANTITY_LIST)
    isStudent = ask_identity() == STUDENT_CODE
    return isStudent

# function to get user selection
def ask_selection():
    while True:
        number = input(f"Please enter your selection (1-{EXIT_CODE-1}) to order, {EXIT_CODE} to exit: ")
        if is_selection_valid(number):
            return int(number)
        else:
            print(ERR_MSG)

# function to determine if selection is valid
def is_selection_valid(number):
    if number.isdigit():
        number = int(number)
        return number >= 1 and number <= EXIT_CODE
    else:
        False

# function to get quantity of the selection
def ask_quantity(selection):
    while True:
        quantity = input(f"Please enter your quantity of {MENU_LIST[selection - 1][0]}: ")
        if quantity.isdigit():
            return int(quantity)
        else:
            print(ERR_MSG)

# function to ask if the user is student or stuff
def ask_identity():
    while True:
        identityNumber = input(f"Please enter your identity({STUDENT_CODE} for student, {STUFF_CODE} for stuff): ")
        if identityNumber.isdigit():
            identityNumber = int(identityNumber)
            if identityNumber == STUDENT_CODE or identityNumber == STUFF_CODE:
                return identityNumber
            else:
                print(ERR_MSG)

# function to compute bill
def compute_bill(isStudent):
    totalBeforeTax = 0
    tax = 0
    for i in range(len(QUANTITY_LIST)):
        if QUANTITY_LIST[i] != 0:
            totalBeforeTax = totalBeforeTax + float(MENU_LIST[i][1]) * QUANTITY_LIST[i]
    if not isStudent:
        tax = totalBeforeTax * TAX_RATE
    return totalBeforeTax, tax

# function to display the recipt
def print_bill(totalBeforeTax, tax):
    print("*" * LENGTH_OF_STAR)
    for i in range(len(QUANTITY_LIST)):
        if QUANTITY_LIST[i] != 0:
            print(f"You have ordered {QUANTITY_LIST[i]} {MENU_LIST[i][0]}")
            print(f"Cost per item is {MENU_LIST[i][1]} and subtotal is {(float(MENU_LIST[i][1]) * QUANTITY_LIST[i]):.2f}")
    print("*" * LENGTH_OF_STAR)
    print(f"Your total before tax: {totalBeforeTax:.2f}")
    print("*" * LENGTH_OF_STAR)
    print(f"Your tax amount:{tax:.2f}")
    print("*" * LENGTH_OF_STAR)
    print(f"Your total after tax:{(totalBeforeTax + tax):.2f}")

# call the main function
main()
