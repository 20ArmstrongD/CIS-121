# name = ["donnie", "armstrong"]

# random_stuff = [1,1.2, False,[], "S"]

# #indexing 
# #lists in python always start counting at 0 (length - 1)
# print(name[1])

# for item in random_stuff:
#     print(item)

# #create a script that creates the sentence of the 2 lists: 
# #list 1 ["I', "your", "dude"]
# #list 2 ["am", "boss", "."]

# part1 = ["I", "your", "dude"]
# part2 = ["am", "boss", "."]

# for word_index in range (0,3):
#     print(part1[word_index], part2[word_index],end=" ")

# #OR 

# part1 = ["I", "your", "dude"]
# part2 = ["am", "boss", "."]

# print(part1[0],part2[0],part1[1],part2[1],part1[2],part2[2])

#problem 2 
#create a function that allows the user to create 2 list of len 5. the user must type in only numbers (int). 
#once all 10 numbers have been added, create a third list with the sum of the same index vlaues 

from curses.ascii import isdigit


def problem2():
    list1 =[]
    list2 = []
    list3 = []

    count = 0   #use count because of the while loop use
    user = input("please enter a number:")
        #
    if user.isdigit(): #check it it a actual digit
            if count < 5:
                list1.append(int(user))
            else: #check if someting is not a deigit
                list2.append(int(user))
            count += 1
    else:
         print("please enter a real number please")
print(list1)
print(list2)
print(list3)
for index in range(0,len(list2)):
    list3.append(list1[index]+list2[index])

    print("list 1:", list1)
    print("list 2:",list2)
    print("sum of list:", list3)


#problem3
#create a script that asks the user for 3 family members.
#then ask them what they rank they give them from 1-3.
#keep track of the rnak in different list
#when asking for rnak make sure to tell them who the rank is for
##what rank do you give oyur mom:
#display a table with the infor

name = []
rank = []
count = 0

while count < 3:
    user_input = input("please enter fmaily member")
    names.append(user_input)
    count+=1 

    if count == 1:





