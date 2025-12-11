#used to hold code for later use

#A1 
def reset():
    status = False
    python = r"\Python314\python.exe"
    script_path = r"Users\natio\Desktop\Projects\pyProjects_Scripts"
    os.execv(python, [python, script_path])

#B1
def whatToDo():
    try:
        task = 0
        task = int(input('1. Balance  2. Take $150 out 3. Change Currency 4. Exit\n'))
    except ValueError:
        print('oops')
    if task == 1:
        bal = balance()
        input('Press Enter to continue or ctrl + C to exit the program\n')
    elif task == 2:
        print('To be done')
        input('Press Enter to continue\n')
    elif task == 3:
        changeBal()
        input('Press Enter to continue\n')
    elif task == 4:
        os.system('cls')
        status = False
    else:
        print('Invalid Input Please Try Again')
        input('Press Enter to continue\n')
    isFirst = False 

#C1
#Checks whether balance has been adjusted at all
def isFirstCheck():
    if isFirst == True:
        print('What would you like to do: ')
    else:
        print('What would you like to do now: ')

#D1
#performs the bal change
#might be benficial to make this a list of some sort might be a quicker then all these if and elif
def changeBalAction(change):
    if change == 1:
        original = total_hun
        total_hun = getHundreds()
        bal = balance - original + total_hun
    elif change == 2:
        print('1')
    elif change == 3:
        print('1')
    elif change == 4:
        print('1')
    elif change == 5:
        print('1')
    elif change == 6:
        print('1')
    elif change == 7:
        print('1')
    elif change == 8:
        print('1')
    elif change == 9:
        print('1')
    elif change == 0:
        print('1')
    return bal

#E1
#allows for small changes to bal
def changeBal():
    os.system('cls')
    print("Current Amount:")
    print("Hundreds: " + str(int(total_hun)) + "   Fifties: " + str(int(total_fif)) + "   Twenties: " + str(int(total_twe)) + "   Tens: " + str(int(total_ten)) + "   Ones: " + str(int(total_one)))
    print("Quarters: " + str(int(total_hun)) + "   Dimes: " + str(int(total_fif)) + "   Nickels: " + str(int(total_twe)) + "   Pennies: " + str(int(total_ten)) + "   Special Amount: " + str(int(total_one)))
    print("What currency type would you like to change:")
    print("1. Hundreds 2. Fifties 3. Twenties 4. Tens    5. Ones ")
    try:
        change = int(input("6. Quarters 7. Dimes   8. Nickels  9. Pennies 0. Special\n"))
    except ValueError:
        print('Invalid Input')
        input('press Enter to continue')
    changeBalAction(change)
    return bal
   