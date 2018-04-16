import hashlib

def isDoor(character):
    door = 0
    if character == "b" or character == "c" or character == "d" or character == "e" or character == "f":
        door = 1
    return door

index = 0
queue = [[0,0, "rrrbmfta"]]

done = False
count = 0
nums = []

while len(queue) != 0:
    newQueue = []
    count += 1
    while len(queue) != 0:
        node = queue.pop(0)
        passcode = node[2]
        hashCode = hashlib.md5(passcode.encode('utf-8')).hexdigest()
        
        up = isDoor(hashCode[0])
        down = isDoor(hashCode[1])
        left = isDoor(hashCode[2])
        right = isDoor(hashCode[3])
        
        # print("up:", up, "down:", down, "left:", left, "right:", right)
        if up and node[1] > 0:
            newNode = [node[0], node[1]-1, passcode+"U"]
            if [newNode[0], newNode[1]] != [3,3]:
                newQueue.append(newNode)
            else:
                nums.append(count)
        if down and node[1] < 3:
            newNode = [node[0], node[1]+1, passcode+"D"]
            if [newNode[0], newNode[1]] != [3,3]:
                newQueue.append(newNode)
            else:
                nums.append(count)
        if left and node[0] > 0:
            newNode = [node[0]-1, node[1], passcode+"L"]
            if [newNode[0], newNode[1]] != [3,3]:
                newQueue.append(newNode)
            else:
                nums.append(count)
        if right and node[0] < 3:
            newNode = [node[0]+1, node[1], passcode+"R"]
            if [newNode[0], newNode[1]] != [3,3]:
                newQueue.append(newNode)
            else:
                nums.append(count)

        
    queue = newQueue
print(nums[-1])

    # print(queue)
    # if len(queue) == 0:
    #     done = True
    # for i in range(len(queue)):
    #     n = queue[i]
    #     if n[0] == 3 and n[1] == 3 and len(queue) == 1:
    #         print(n)
    #         done = True
            
