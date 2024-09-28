def printfactors(number):
    print("THE FACTORS OF...>", number, "ARE")
    for i in range(1, number+1):
        if number % i == 0:
            print(i)
number = int(input("ENTER A NUMBER TO FIND ITS FACTORS"))
printfactors(number)