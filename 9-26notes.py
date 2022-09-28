            
#             #0          #1
names = ["donnie","armstrong"] #this is a list

random_stuff = ["don", 1, 122.3, False,[]] #string, integer,boolean, 

print(names[0])
print(random_stuff[2])

#LAST VALUE
print(names[-1])

for value in random_stuff:
    print(value)

#create a script that goes through this list [2,45,32,43,22] and display the square of every number
practice = [2, 45, 32, 43, 22]

result = []



for num in practice:
    result.append(num**2)
print(result)

#to know wlngth of list 
# print(len(result))

name = input("what is your name:")
age = int(input("what is your age:"))
your_number = int(input("what is your number:"))

info = [name,age,your_number]
print("name:" , info[0])
print("age:", info[1])
print("Number:", info[2])

#Create a script that creates a list without the number 20 in it from the list 
# [20,34,23,2,11,24,4,20,21,12,20,20,20]

my_number = [20,34,23,2,11,24,4,20,21,12,20,20,20]

clean = []

for number in my_number:
    if number != 20:
        clean.append(number)

print(my_number)
print(clean)


   