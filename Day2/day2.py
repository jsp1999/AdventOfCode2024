reports = []

with open('data.txt', 'r') as file:
    for line in file:
        report = list(map(int, line.split()))
        reports.append(report)

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

def checkLevel(level):
    is_increasing = all(level[i] <= level[i+1] for i in range(len(level)-1))
    is_decreasing = all(level[i] >= level[i+1] for i in range(len(level)-1))
    
    if not is_increasing and not is_decreasing:
        return False
    
    for i in range(1, len(level)):
        if abs(level[i] - level[i - 1]) > 3 or abs(level[i] - level[i - 1]) < 1:
            return False

    return True

def checkLevelWithDampener(level):
    if checkLevel(level):
        return True
    else:
        for i in range(len(level)):
            newLevel = level[:i] + level[i+1:]  
            if checkLevel(newLevel):
                return True

        return False

safe_reports = list(filter(checkLevel, reports))
dampened_reports = list(filter(checkLevelWithDampener, reports))

print(len(safe_reports))
print(len(dampened_reports))