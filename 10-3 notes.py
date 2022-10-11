names = ["Donnie", 2,2.3,23]

print(names[2])


#empty dictionary
info = {}

info = {
    "patient 0" : ["Donnie", "armstrong", 23],
    "patient 1": 23,
    "patient 2": ["bob", "builder", 123]
}

#how to add values to dictionary 
info["patient 3"] = "roger", "NA", "NA"


print(info["patient 3"])


# #create scrip that ask user for namme, last, age, and keep this stored in dictionary, then print out the values
name = input("what is your name:")
last_name = input("what is your last name:")
age = input("what is your age:")

info = {
    name : [name,last_name,age]
}

print("hi your name is", info[name][0]+" "+info[name][1],"you are ", info[name][2], "years old")


# create a script that asks the user for 5 soccer palyers and how many goals they have made this season(in a dictionary).
# calculate the avg in seaprate function


def average_Goals(players):
    sum = 0
    for player in players:
        sum += players[player]

    return sum/len(players)

players = {}

for i in range(5):
    soccer_player_name = input("name a soccer player: ")
    goals = int(input("how many goals did they score this season: "))

players[soccer_player_name] = goals

print("the average goals was: ", average_Goals(players))


#create a function capable of identifying if a key exists in your dictionary 
info = {
    "test" : 0,
    "test 1" : 1,
    "test 2" : 2, 
 }

def check_keys(data,key):

    for keys in data:
        if keys == key:
            return True

    return False

print(check_keys(info,"test 1"))
#
info1 = {
    "data" : [1,2,3,4,5]
}

info2 = {
    "data" : [6,7,8,9,10]
}

def add_together(data,data2):
    total = []
    for i in range(len(data["data"])):

        total.append(data["data"][i]+data2["data"][i])

    print(total)

add_together(info1,info2)