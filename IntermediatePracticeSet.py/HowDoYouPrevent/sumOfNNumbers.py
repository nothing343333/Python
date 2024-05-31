def additon():
    x = input("enter the number of which you find till total summation of\n")
    if x == 0 or x == 1:
        return 1
    else:
        result = x*summation(x-1)
        return result
    

    print(result)

    additon()