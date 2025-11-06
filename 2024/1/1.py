#Solution path:
#   1. Get locations from saved file and parse them into 2 lists
#   2. Sort both lists in ascending order
#   3. Count the distance between 2 locations for all adjacent positions while adding them to a "total distance counter"
#   4. Write total distance in "answer.txt"

# Not gonna bother with any fancy program structure here. Should be quick and easy.

#######################################
# 1
locations = open("lists/locations.txt", "r")

# Define lists to store locations
leftList = []
rightList = []

# parse locations into lists
for line in locations:
    leftList.append(int(line.split()[0]))
    rightList.append(int(line.split()[1]))
locations.close()

#######################################
#2
# sort lists
leftList.sort()
rightList.sort()

#######################################
#3
totalDistance = 0
# count total distance
for i in range(len(leftList)):
    totalDistance += abs(leftList[i]-rightList[i])

#######################################
#4
# write answer to file
answer = open("answer.txt", "w")
answer.write(str(totalDistance))
answer.close()
print(totalDistance)
