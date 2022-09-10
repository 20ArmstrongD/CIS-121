
9-8-2021

tax0wed = 0.0

earnedincome = float(input("enter the amount of income you earned in 2021: "))
if earnedincome < 0:
    print("you made less than $0. you probably need to go to a accountant or a bank")
    sys.exit()

if earnedincome < 11000:
            tax = 0
elif earnedincome > 11000 and earnedincome < 43000:
        tax = (0.2 * income) - 2200
elif earnedincome > 43000 and earnedincome < 150000:
        tax = (0.4 * (earnedincome - 43000)) + 6400
elif earnedincome > 150000:
        tax = ((earnedincome - 150000) * 0.45) + 6400 + 42800


print("Are you married or single?")
maritalstatus = input("Type m for married and s for single: ")


#Ensures you have a valid martial stsus
while maritalstatus != "m" and maritalstatus != "s":
    print("you enterd and invalid martial status")
    maritalstatus = input("Type m for married and s for single: ")