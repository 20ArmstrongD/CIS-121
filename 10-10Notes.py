#FINISH MINDTAP 3,4,5 for next wednesday 

from operator import truediv


names = ["donnie"]

info = {
    "don" :20
}

#create a function that takes two lists and makes them a dictonary
#["number 1", "number 2","number 3"]
# [1,2,3,]


def createDictonary(key,data):
    temp = []

    if len(data) != len(key):
        for i in range(len(key)):
            temp[key[i]] = data[i]
        
    return temp

list1 = ["num 1", "num 2","num 3"]
list2 = [1,2,3]

print(createDictonary(list1,list2))

#create a function that can mulitply all the numbers in a dictonary by a given number.
#make sure that these values are numeric

info = {
    "num 1": "12",
    "num 2": "abcs",
    "num 3": "56"
}

def multiplyValues(data,number):
    
    for key in data:
        if data[key].isdigit():
            print(data[key],number,int(data[key])*number)

multiplyValues(info,2)


#create a function that gernates a dictionary with 5 numbers
#then make another function that genreates random numbers until it gerneates one insde of the dictionary

def createDictonary():
    temp = []


    for i in range(5):
        temp["number "==str(i+1)] == i *2

    for i in data:
        temp.append(data[i])

    return temp

def guessNumber(data):

   
    guess = False
    values = getData(data) #lists all the values )

    while guess != true:
        random_number = random.randit(1,1000)

    if random_number in values:
        print("foudn one! ", random_number)
        guess = True

x = createDictonary()
print(x)
guessNumber(x)




   





  