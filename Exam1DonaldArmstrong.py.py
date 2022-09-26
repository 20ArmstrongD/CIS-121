#1A doesnt work because random_number is a string not an integer

#1B doesn't work because at that point in the code number is not defined and is infinate
#1c it will run because number is defined within the code snippet
#1d will not run because print is not properly indented
#1e needs to be an integer input
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
# milk =  int(input("how much milk dod you buy?:"))
# eggs = float(input("how much eggs did you buy?:"))
# bacon = float(input("how much bacon did you buy?:"))

# subtotal = milk * milkcost + eggs * eggscost + bacon * baconbost
# taxamt = subtotal * 0.11
# total = subtotal + taxamt
# print("you bought", milk, "milks,", eggs, "eggs, and", bacon, "bacon" )
# print("your subtatal is",subtotal)
# print("your tax", taxamt)
# print("your total is $", total)

#problem 3

# def numberNice():

#     number = input("please enter your number:")

    # print("(",number,[0:3],"(", number[3:6],"")
# import numbers
# from random import random


# def formatphone(number): 
#     # validate your input
#     strnum = str(number) #converts input of number into a string
#     if len(strnum) != 10: 
#         print("give me number 10 digits long")
#         return

#     areacode = strnum[0:3] #for lines 58-60 splices or specifiys what numbers it takes
#     firstpart = strnum[3:6]
#     secondpart = strnum[6:10]


#     print("(" + areacode + ") "+ firstpart +"-"+ secondpart) 

# formatphone("7875551212")
# formatphone(7875551212)


    # numbe = str(input("please enter your phone number "))
# 2


#problem 4
def randnums(): #definition for function
    
    for i in range (1,60): #assisns a range for random number(i)
        if (48 % i == 0): #test if i is divisor of 48
           
            if i % 2 == 0: #test if i is even
                print(i)
            if i >= 15: # test if i numbers are greater that 15 
                print("I generated the number", i, ", randomly")
randnums()

# randnums() 

# def askUserForNumber():
#     number = int(input("choose a number:"))
#     return number

# number = askUserForNumber()
# for number in range (1,60):
#     print(number)

# while(number,60):

#     if number <= 15:
#         print("i generated the number", number,", randomly")

# #     elif number % 2 ==0:
# #         print("this is an even number")


# # w = 20
# # n = int(input("enter an upper bound for a check: "))
# # print("between 1 and",n, "there are")  

# # while (w,n):
# #     while (n,w):
# #         if n % w ==0:
# #             print(n," not proper devisor")
#             n+=1

#did my best with these last couple problem but really not understadning how to do them and havn't had the time for mavpass

       



