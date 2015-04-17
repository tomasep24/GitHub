def Main():

    employeeName = input( "What is the employees name: " )
    maritalStatus = input( "Are You Married or Single? " )
    hourlyRate = int(input( "Hourly rate is: " ))
    hoursWorked = int(input( "Hours worked (week): " ))

    grossPay = CalGrossPay(hourlyRate,hoursWorked)
    socialSecurity = TotalSocialSecurityTax(hourlyRate,hoursWorked)
    federalTax = Status(maritalStatus)
    netPay = grossPay - socialSecurity + federalTax

    print ( "Employee: ", employeeName)
    print ( "Net pay for employee: $",format(netPay,",.2f"),sep= "")
    
def CalGrossPay(hourlyRate,hoursWorked):

    grossPay = hourlyRate * hoursWorked
    return grossPay

def TotalSocialSecurityTax(hourlyRate,hoursWorked):

    grossPay = CalGrossPay(hourlyRate,hoursWorked)

    if grossPay <= 2000:
        socialSecurityTax = grossPay * .062
    else:
        socialSecurityTax = 124
    return socialSecurityTax

def Status(maritalStatus):

    if maritalStatus == "Married":
        federalTax = MarriedTax(hourlyRate,hoursWorked)
    else:
        federalTax = SingleTax(hourlyRate,hoursWorked)
    return federalTax

def MarriedTax(hourlyRate,hoursWorked):

    grossPay = CalGrossPay(hourlyRate,hoursWorked)

    if grossPay < 900:
        federalTax = grossPay * .18
    elif grossPay < 9000:
        federalTax = grossPay * .25
    else:
        federalTax = grossPay * .35
    return federalTax

def SingleTax(hourlyRate,hoursWorked):

    grossPay = CalGrossPay(hourlyRate,hoursWorked)

    if grossPay < 500:
        federalTax = grossPay * .15
    elif grossPay < 1000:
        federalTax = ((grossPay - 500) * .20) + 75
    else:
        federalTax = ((grossPay - 1000) * .25) + 175
    return federalTax
    
Main()
