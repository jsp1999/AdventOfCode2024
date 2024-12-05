from functools import reduce

rules = []
updates = []

with open('data.txt', 'r') as file:
    for line in file:
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

def checkUpdate(update):
    for u in update:
        matching_tuple = [t for t in rules if u in t]
        for t in matching_tuple:
            if all(x in update for x in t):
                if update.index(t[0]) > update.index(t[1]):
                    return False
    return True

def getMedianSums(updates):
    return reduce(lambda acc, update: acc + update[len(update) // 2], updates, 0)

def orderUpdate(update):
    changed = True
    while changed:
        changed = False
        for t in rules:
            if all(x in update for x in t):
                first = update.index(t[0])
                second = update.index(t[1])
                if first > second:
                    update[first], update[second] = update[second], update[first]
                    changed = True
    return update

correct_updates = [update for update in updates if checkUpdate(update)]
incorrect_updates = [update for update in updates if not checkUpdate(update)]
incorrect_updates_ordered = [orderUpdate(update) for update in incorrect_updates]

print(getMedianSums(correct_updates))
print(getMedianSums(incorrect_updates_ordered))
