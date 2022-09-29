import DonaldArmstrongStats

file = open("500DayFruitData.txt",'r')
#getting the lines and separating them by /n
data = file.read().splitlines()
data.pop(0)
apple_tracker = []
banana_tracker = []
strawberry_tracker = []
mean = 0
median = 0 

for item in data:
    temporary = item.split()

    if temporary[1]  == "apple":
        apple_tracker.append(int(temporary[2]))

    if temporary[1] == "banana":
        banana_tracker.append(int(temporary[2]))
    
    if temporary[1] == "strawberry":
        strawberry_tracker.append(int(temporary[2]))
    


print(apple_tracker)
print(banana_tracker)
print(strawberry_tracker)

mean = DonaldArmstrongStats.mean(apple_tracker)
median = DonaldArmstrongStats.median(apple_tracker)
mean_Ban = DonaldArmstrongStats.mean(banana_tracker)
median_Ban = DonaldArmstrongStats.median(banana_tracker)
mean_Straw = DonaldArmstrongStats.mean(strawberry_tracker)
median_Straw = DonaldArmstrongStats.median(strawberry_tracker)

print("The mean of the number of apples eaten",DonaldArmstrongStats.mean(apple_tracker))
print("the median of the number of apples eaten",DonaldArmstrongStats.median(apple_tracker))
print("The mean of the number of bananas eaten",DonaldArmstrongStats.mean(banana_tracker))
print("the median of the number of bananas eaten",DonaldArmstrongStats.median(banana_tracker))
print("The mean of the number of strawberries eaten",DonaldArmstrongStats.mean(strawberry_tracker))
print("the median of the number of strawberries eaten",DonaldArmstrongStats.median(strawberry_tracker))

#creating a new file 
with open("Donald_Armstrong_Output.txt",'w') as f:
    f.write("the mean number of apples eaten "+ str(mean)+ "\n"+"\n"+"The mean of the number of apples eaten "+str(median))
    f.write("the mean number of bananas eaten "+ str(mean_Ban)+ "\n"+"\n""The mean of the number of bananas eaten "+str(median_Ban))
    f.write("the mean number of strawberries eaten "+ str(mean_Straw)+ "\n"+"\n""The mean of the number of strawberries eaten "+str(median_Straw))
    

