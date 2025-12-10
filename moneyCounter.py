import os
import sys

#some public variables
total_pen = 0.0
total_nic = 0.0
total_dim = 0.0
total_qrt = 0.0
total_one = 0.0
total_fiv = 0.0
total_ten = 0.0
total_twe = 0.0
total_fif = 0.0
total_hun = 0.0
total_coin_amount = 0.0
total_dol_amount = 0.0
total_amount = 0.0
bal = 0.0
status = True
isFirst = True

#lets users input how many of each currency they have
def getAmount(Type):
    try:
        amount =  int(input("How many " + Type + " do you have: ")) 
    except ValueError:
        print("Invalid Input")
        input("Press enter to continue")
    if amount < 0:
        print("Negative Number Input Returning to Main Menu.")
        input("Press enter to continue")
        reset()
    return amount
        
#pennies section
def getPennies():
    pen = getAmount("Pennies")
    total_pen = pen * .01
    return total_pen

#nickels section
def getNickels():
    nic = getAmount("Nickels")
    total_nic = nic *.05
    return total_nic

#dimes section
def getDimes():
    dim = getAmount("Dimes")
    total_dim = dim *.1
    return total_dim

#quarters section
def getQuarters():
    qrt = getAmount("Quarters")
    total_qrt = qrt *.25
    return total_qrt

#ones section
def getOnes():
    total_one = getAmount("One Dollar Bills")
    return total_one

#fives section
def getFives():
    fiv = getAmount("Five Dollar Bills")
    total_fiv = fiv * 5
    return total_fiv

#tens section
def getTens():
    ten = getAmount("Ten Dollar Bills")
    total_ten = ten * 10
    return total_ten

#twenties section
def getTwenties():
    twe = getAmount("Twenty Dollar Bills")
    total_twe = twe * 20
    return total_twe

#fifties section
def getFifties():
    fif = getAmount("Fifty Dollar Bills")
    total_fif = fif * 50
    return total_fif

#Hundred section
def getHundreds():
    hun = getAmount("Hundred Dollar Bills")
    total_hun = hun * 100
    return total_hun

#gets all amounts, calculates balance and prints
def balance():
    total_pen = getPennies()
    total_nic = getNickels()
    total_dim = getDimes()
    total_qrt = getQuarters()
    total_one = getOnes()
    total_fiv = getFives()
    total_ten = getTens()
    total_twe = getTwenties()
    total_fif = getFifties()
    total_hun = getHundreds() 
    total_coin_amount = total_pen + total_nic + total_dim + total_qrt
    total_dol_amount = total_one + total_fiv + total_ten + total_twe + total_fif + total_hun
    bal = total_dol_amount + total_coin_amount
    print("Your total balance is: " + str(bal))  

#amount in cash
def cashAmount():
    total_amount = total_dol_amount + total_coin_amount 

#amount in coins
def coinAmount():
    total_coin_amount = total_pen + total_nic + total_dim + total_qrt

#allows for small changes to bal
def changeBal():
    print("What currency type would you like to change:")
    print("1. Hundreds 2. Fifties 3. Twenties 4. Tens    5. Ones ")
    try:
        change = int(input("6. Quarters 7. Dimes   8. Nickels  9. Pennies 0. Special\n"))
    except ValueError:
        print('Invalid Input')
        input('press Enter to continue')

#Checks whether balance has been adjusted at all
def isFirstCheck():
    if isFirst == False:
        print("Your balance is $" + str(bal))
        print('What would you like to do now: ')
    print('What would you like to do now: ')

#includes the header of the terminal
def pretext():
    os.system('cls')
    print('Press ctrl + C to exit at any time.') 
    isFirstCheck()

#In the works
def reset():
    status = False
    python = r"\Python314\python.exe"
    script_path = r"Users\natio\Desktop\Projects\pyProjects_Scripts"
    os.execv(python, [python, script_path])

#add back in later
#def whatToDo():
    

while status == True:
    pretext()
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
    os.system('cls')


#Current limitations 
# 1. Amount can not exceed int digit limit (not a big worry)
# 2. does not ask about $2 bills or special coins (eh uncommon but could add a special add tab )