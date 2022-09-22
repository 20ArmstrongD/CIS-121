
sheep= int(input("how many sheep do you have?:"))
    
if(sheep == 0):
    print("put valid number of sheep")
    main()

white = 0
brown = 0
black = 0

for x in range(sheep):
    if(x % 3 ==0 or x % 4 == 0):
        brown += 1
        
    elif (x % 2 == 0):
        white += 1

    else:

        black += 1
    print("kevin has", white,"white sheep", black,"black sheep", brown, "brown sheep")
