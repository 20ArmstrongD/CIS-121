#1A doesnt work because random_number is a string
#1B doesn't work because at that point in the code number is not defined
#1c
#1d
#1e code runns forever shound ad print user number along with end
# name = input("please enter your name:")
# age = input ("please enter your age: ")

# random_number =  10 /(age%23)

# while number <100:
#     print(number)

# number = 5

# if number <3:
#     print("Less")
# elif number > 3:
#     print("greater")
# else:
#     print("SAME")

# for i in range(1,10):
#     print(i)

# user_number = 0

# while user_number != 5:
#     user_number = input("please enter a number:")


#problem 2
# milkcost = 2.00
# eggscost = 1.50
# baconbost = 3.00
# milk =  float(input("how much milk dod you buy?:"))
# eggs = float(input("how much eggs did you buy?:"))
# bacon = float(input("how much bacon did you buy?:"))

# total_cost = milk * milkcost + eggs * eggscost + bacon * baconbost
# print("you bought", milk, "milks,", eggs, "eggs, and", bacon, "bacons.")
# print("your total is $", total_cost)

#problem 3

# def askUserForPhone():
#     number = input("please enter your phone number ")
#     return number
# number = askUserForPhone()
# print(number)
# number2 = askUserForPhone()
# print(number2)

phone_number = 7875551212
print("(787)-555-1212")

# #for number in phone_number:
#     print(number)

#problem 4
def askUserForNumber():
    number = int(input("choose a number:"))
    return number

number = askUserForNumber()

for number in range (1,60):
    print(number)

while(number,60):

    if number <= 15:
        print("i generated the number", number,", randomly")

    elif number % 2 ==0:
        print("this is an even number")


w = 20
n = int(input("enter an upper bound for a check: "))
print("between 1 and",n, "there are")  

while (w,n):
    while (n,w):
        if n % w ==0:
            print(n," not proper devisor")
            n+=1
       



