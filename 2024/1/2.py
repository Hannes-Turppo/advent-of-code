import json

# first we need to get the sorted lists from already stored files:
def getLists(target):
    with open(target, "r") as file:
        lists = json.load(file)
        file.close()
    return lists

# then we will need to count exactly how many times each element from left appears from right
def countSimilarity(lists):
    similarity = 0
    for item in lists["left"]:
        while item >= lists["right"][0]:
            if item == lists["right"][0]:
                similarity += item
            lists["right"].pop(0)
    return similarity


# main
def main():
    lists = getLists("lists/sorted.json")
    similarity = countSimilarity(lists)
    print(similarity)
    return

# run
main()
