# while loop:
# use when you have condition like stoping at a certain point
# number = 0 
# while number <= 10:
#     print(number)
#     number +=1

#number % 2 == 0: is for finding even number
#number % 2 == 1: is for finding if number is odd

# # #for loop
# # for or i are the same
# # use for beggining to end 
# # you can use for and while loops for same results
# for number in range(1,11):
#     print(number)

# for number in range(1,11):
#     if number % 2 == 0:
#         print(number)

#function 
#def means define
#when writing a function lowercase the first letter of the word then captialize the first leter of every word
#scope
# def askUserForName():
#     name = input("please enter your name: ")
#     return name
# name = askUserForName()
# print(name)
# name2 = askUserForName()
# print(name2)

#create a function that asks the user for their age. then use that value to priont out the next 20 years (use a for loop)

# def askUserForAge():
#     age = int(input("please enter your age"))
#     return age

# age = askUserForAge()

# for number in range(age,age+21):
#      print(number)


#string Manipulation
name = "Donnie"
print(name[0:5])
     

for letter in name:
    print(letter)



user = int(input("how many dvds: "))

summ = user *3 

if summ >= 50:
    print("you pay", summ - summ * .2)
if summ >= 30:
    print ("you pay", summ - summ * .1)

# user = int(input("enter a number:" ))

# if user == 1:
#     print(user)
# if user ==1:
#     print(user, user * 2)
# if user ==1:
#     print(user, user * 2, user * 3)
# if user ==1:
#     print(user, user * 2,+ user  * 3, user * 4)
# if user ==1:
#     print(user, user * 2, user * 3, user * 4, user * 5)

# thes 2 for loops allow me to go level by level
# for i in range(1,7): #level manager
#     for j in range(1,i): #
#         print(j, end="")
#     print(" ")