# It seems the problems might be related to each other and having the left and right lists available in sorted form would be useful.
# Let's make files that contain the lists in useful forms.
import json

# parse locations into lists
def getLists():
    lists = {
        "left":[],
        "right":[]
    }

    with open("locations.txt", "r") as locations:
        for line in locations:
            lists["left"].append(int(line.split()[0]))
            lists["right"].append(int(line.split()[1]))
        locations.close()

    return lists

# Write lists into file
def writeLists(lists, target):
    with open(target, "w") as file:
        lists_json = json.dumps(lists)
        file.write(lists_json)
        file.close()
    return True

# sort lists
def sortLists(lists):
    return {
        "left": sorted(lists["left"]),
        "right": sorted(lists["right"])
    }

# main
def main():
    lists = getLists()
    sorted = sortLists(lists)
    writeLists(lists, "original.json")
    writeLists(sorted, "sorted.json")
    return

main()
