def main():

    courseCost = int(input( "What is the cost per Course at ACC:" ))
    creditCost = int(input( "What is the cost per credit hour at Texas State:" ))
    termInYears = int(input( "Number of years attended:" ))
    flatCost= int(input( "What is the Flat fee at Texas States?" ))
    acc = (30 / 3) * courseCost
    texasState = creditCost * 30 + flatCost
    dif =  texasState - acc

    accTotal = 0
    texasStateTotal = 0
    differenceTotal = 0
    
    print("Year\tACC\t\tTexas-State\tDifference")        

    for termInYears in range (1, 5):

        if termInYears > 2:

            dif += acc
            acc = 0

        accTotal += acc 
        texasStateTotal += texasState
        differenceTotal += dif 
                
        print(format( termInYears, "4d"),"\t",
              format( accTotal, ",.2f"),"\t",
              format( texasStateTotal, ",.2f"),"\t",
              format( differenceTotal, ",.2f"), sep="")

main()

