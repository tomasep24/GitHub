def main():

    customer = input( "Is there customer (Y/N)?") 

    while customer == "Y":
    
            books = int(input( "How many books were purchase?" ))
            sciFi = int(input( "How many Sci-Fi books were purchase?" ))
            points = bookPoints(books) + sciFiPoints(sciFi)
            status = 0
            print( "You earned", points, "points.")
        
            if points >= 100:
                print( "You are a premier Customer.")
            else:
                print( "You are not a premier Customer.")
            customer = input( "Is there customer (Y/N)?")
            
def bookPoints(books):

    if books <= 2:
        points = 0
    elif books <= 9:
        points = 50
    elif books >= 10:
        points = 10 * books
    return points

def sciFiPoints(sciFi):

    if sciFi >= 0:
        points = 8 * sciFi
    return points

main()
