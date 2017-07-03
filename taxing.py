#!/usr/bin/python3

'''
This script is used to calculate your income after tax in NZ.
It also calculates the income after both tax and student loan repayment.
As of July 2017.
'''

# These dictionaries need to be updated with changing tax laws
brackets = {range(1, 14001):0.105, range(14001, 48001):0.175,
             range(48001, 70001):0.300, range(70001,1000000):0.330}
dictRange = (range(1, 14001), range(14001, 48001), 
             range(48001, 70001), range(70001,1000000))

# Function for calculating tax in current tax bracket
def current_bracket_tax(taxRange, bVal):
    bracketMin = min(list(taxRange)) - 1
    bracketAT = (bVal - bracketMin) * brackets.get(taxRange)
    return bracketAT

# Function for calculating max tax in current tax bracket
def other_bracket_tax(taxRange):
    bMin = min(list(taxRange)) - 1
    bMax = max(list(taxRange))
    bAT = (bMax - bMin) * brackets.get(taxRange) 
    return bAT

# Function calculates total tax
def calc_tax(BIncome):
    totalTax = 0
    for key in dictRange:
        if BIncome in key:
            totalTax += current_bracket_tax(key, BIncome)
            break
        else:
            totalTax += other_bracket_tax(key)
    return totalTax

# Function for asking if you have a student loan
def studentLoan():
    yes = ("Y", "YES", "TRUE")
    no = ("N", "NO", "FALSE")
    status = str(input("Do you have a student loan? "))
    while status.upper() not in (yes + no):
        status = str(input("The answer must be yes or no: "))
    if status.upper() in yes:
        return True
    elif status.upper() in no:
        return False

# Function tests whether a string can be converted to a float
def is_num(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Function asks your annual income
def grossIncome():
    annualIncome = input("What is your annual income? $")
    numTest = is_num(annualIncome)
    while not numTest:
        annualIncome = input("Answer must be numeric: $")
        numTest = is_num(annualIncome)
    return float(annualIncome)

def calcLoan(BIncome):
    overThreshold = BIncome - 19136.00
    repayment = overThreshold*0.12
    return repayment



#This section runs the script

print("\nThis script determines your income after tax.")
print("It will also deduct a student loan repayment if you have one.\n")

hasLoan = studentLoan()
beforeTax = grossIncome() 

print("")

totalTax = calc_tax(beforeTax)

if hasLoan:
    loanPayment = calcLoan(beforeTax)
else:
    loanPayment = 0.0

afterTax = beforeTax - totalTax - loanPayment

afterTaxDP = round(afterTax, 2)

print("Your income after deductions is $" 
      + str.format('{0:.2f}', afterTaxDP) 
      + ", your tax is $" 
      + str.format('{0:.2f}', totalTax) 
      + ", and your student loan repayment is $" 
      + str.format('{0:.2f}', loanPayment)
      + "."
     )

weekly = afterTax/52.0

print("Your weekly income is $" + str.format('{0:.2f}', weekly) + ".\n")
