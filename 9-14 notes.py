
    

from ast import While


name = "donnie" # str
number = 1 # int
distance = 1.2 # float
finished = True #boolean #boolean True and False, first letttter must be capitalized

print("donnie")
print(name,number,distance)


if number > 10:
    print("this is thing")
elif number < 10: #is used when you have multiple scenerios like 
    print("this is not thing")
else: #
    print ("this is not thing")

if number > 10:
    print("LOL")
if number < 10:
    print("nah")

#while
while number <= 10:
    print(number)
    number +=1

#write a script that keeps asking the user for a number and check if the number is even or odd. let the user know what it is. If they enter the number 0 stop asking for numbers.
done = False

while done != True:
    number = int(input("please enter a number:" ))
    if number == 0:
        print("yay!")
        done = True 
    elif number % 2 == 0:
        print("this a even number")
    else:
        print("this a odd number")
       
# Create a script that sks the user for their name and income. let the user know how much money they would have if they don't spend any money in 20 years.
# hey _name_, you make _income_ a year!
# this is how much money you would have in 20 years
# 40000 year 1
# 80000 year 2

name = input("please enter your name:")
income = int(input("please enter your income:"))

print("hey",name, "you make" ,income, "a year")
print("this is what you could make in 20 years")

done = False  
years = 1
money = 0
while done != True:
    money = income*years
    print("$"+str(money), "year", years)

    years +=1

    if money >=10000:
        done = True

# let the user know how many years until they have save 10,000
