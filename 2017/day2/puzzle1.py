with open("input.txt") as f:
    content = f.readlines()
content = [x.split() for x in content]

## Puzzle 1

counter = 0

for i in range(len(content)):
    maxNum = int(content[i][0])
    minNum = int(content[i][0])
    for j in range(len(content[i])):
        if int(content[i][j]) > maxNum:
            maxNum = int(content[i][j])
        if int(content[i][j]) < minNum:
            minNum = int(content[i][j])

    counter += maxNum-minNum

print(counter)

## Puzzle 2

counter2 = 0

for i in range(len(content)):
    listLength = len(content[i])
    for j in range(listLength):
        for k in range(listLength):
            if j != k:
                if int(content[i][j]) % int(content[i][k]) == 0:
                    counter2 += int(content[i][j]) / int(content[i][k])



print(counter2)