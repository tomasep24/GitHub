def Main():

    employeeName = input( "What is the employees name: " )
    maritalStatus = input( "Are You Married or Single (Y or N)? " )
    hourlyRate = int(input( "Hourly rate is: " ))
    hoursWorked = int(input( "Hours worked (week): " ))

    grossPay = hourlyRate * hoursWorked
    socialSecurity = TotalSocialSecurityTax(grossPay)

    if maritalStatus == "Y":
        federalTax = MarriedTax(grossPay)
    elif maritalStatus == "N":
        federalTax = SingleTax(grossPay)
    else:
        print ("error")
        return Main()

    netPay = grossPay - (socialSecurity + federalTax)

    print ( "Employee: ", employeeName)
    print ( "Federal Tax: $", format(federalTax,",.0f"),sep="")
    print ( "Net pay for employee: $", format(netPay,",.0f"),sep= "")

def TotalSocialSecurityTax(grossPay):

    if grossPay <= 2000:
        socialSecurityTax = grossPay * .062
    else:
        socialSecurityTax = 124
    return socialSecurityTax

def MarriedTax(grossPay):

    if grossPay < 900:
        federalTax = grossPay * .18
    elif grossPay < 9000:
        federalTax = grossPay * .25
    else:
        federalTax = grossPay * .35
    return federalTax

def SingleTax(grossPay):

    if grossPay < 500:
        federalTax = grossPay * .15
    elif grossPay < 1000:
        federalTax = ((grossPay - 500) * .20) + 75
    else:
        federalTax = ((grossPay - 1000) * .25) + 175
    return federalTax
    
Main()
