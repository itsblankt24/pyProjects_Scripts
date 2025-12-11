import os
#import sys

#might be a good project to learn more about oop but lets get it working 
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
printBalance = 0.0

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
    return bal

#amount in cash
def cashAmount():
    total_amount = total_dol_amount + total_coin_amount 

#amount in coins
def coinAmount():
    total_coin_amount = total_pen + total_nic + total_dim + total_qrt

#includes the header of the terminal
def pretext(printBalance):
    os.system('cls')
    print('Press ctrl + C to exit at any time.') 
    print("Your balance is $" + str(printBalance))
    #isFirstCheck()

#to simplify the continue button  
def toContinue():
    input('Press Enter to continue\n')

#the input that determines task
def taskPrompt():
    try:
        task = 0
        task = int(input('1. Balance  2. Take $150 out 3. Change Currency 4. Exit\n'))
    except ValueError:
        print('oops')
    return task

def performTask(task):
    bal = 0.0
    notStop = True
    if task == 1:
        os.system('cls')
        bal = balance()
        input('Press Enter to continue \nor ctrl + C to exit the program\n')
    elif task == 2:
        print('in the works')
        toContinue()
    elif task == 3:
        #changeBal()
        print('To be done')
        toContinue()
    elif task == 4:
        os.system('cls')
        print("Shutting Down")
        toContinue()
        notStop = False
        os.system('cls')
    else:
        print('Invalid Input Please Try Again')
        toContinue()
    return notStop, bal
     
while status == True:
    pretext(printBalance)
    task = taskPrompt()
    status, printBalance = performTask(task) 


#In the works: A1 reset()

#In the works: B1 whattodo()

#to be continued: C1 isFirstCheck()

#to be continued: D1 changeBalAction()

#to be continued: E1 changeBal()

#Current limitations 
# 1. Amount can not exceed int digit limit (not a big worry)
# 2. does not ask about $2 bills or special coins (eh uncommon but could add a special add tab )