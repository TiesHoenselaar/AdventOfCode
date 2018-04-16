positions = [13, 17, 19, 7, 5, 3, 11]
currentPos = [10, 15, 17, 1, 0, 1, 0]


position = [-1, -1, -1, -1, -1, -1, -1]
time = 0

while position != [0, 0, 0, 0, 0, 0, 0]:
    time += 1
    for i in range(1,len(positions)+1):
        position[i-1] = (i + time + currentPos[i-1])%positions[i-1]
    
print(time)