#docs.python.org
#really good resource.
# THIS CAN BE USED IN THE EXAMS!!!!

names = ["kendrick","armstrong"]

info = {
    "kendrick" : 23,
    "bob" : 2345
}



#open a file
file = open("data.txt",'r')

#to get the data from the file, remeber everything from a file is considered a string
data = file.read().splitlines()

print(data)

#Create a function that takes a list of values in str and return a new list with only int.
def str_to_int(data) :
    temp = []

    for number in data:
        if number.isdigit():
            temp.append(int(number))
    return temp

print(str_to_int(data))

#create a function that takes numbers then adds 5 to them.

def str_add_five(data):
    temp = []

    for number in data:
        temp.append(str(number))
    return temp

print(str_add_five(data))


#write the results to a new file

with open("results_.txt","w") as f:
    for number in data:
        f.write(str(number) + "\n") 

#genreate a random number
# a = rand.randint(1,100)
# print(a)

# #part 1
# #gernate a list with 100 random values
# #then write the vlaues to a file calle "random_numbers_generated.txt"

rand = []

for i in range(100):
    rand.append(random.radiant(1,100))

#writing to file
write_to_file(rand,"random_numbers_generated")

a = random.randint(1,100)
# print(a)

#part 2
#generate a function that counts how many times each number appears
#use a dictionary to keep track

def count_num(data):

    temp = {}

    for number in data:
        if number in temp:
            pass
        else:
            temp[str(number)] = data.count(number)
    return temp

print(count_num(rand))



#part C
#write the info from disctionary to a file calles "final.txt"

with open("final.txt"'w') as f:
    for key in c:
        f.write(key+":"+str(c[key])+'/n')