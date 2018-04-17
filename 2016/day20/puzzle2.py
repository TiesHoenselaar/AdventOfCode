

# a1 = 2803551464
# a2 = 2812875810

# b1 = 3863319608
# b2 = 3871068145



# blocked = [[5, 8], [10, 12], [16, 18], [30, 50]]
blocked = [[2803551464, 2812875810]]

# insert = [10, 12]
# insert = [20, 25]

count = 0
def insertRange(blockedList, insert, count):

    if insert[1] < blockedList[0][0]:
        print('a')
        count += 1
        blockedList = [insert] + blockedList
    elif insert[0] > blockedList[-1][1]:
        print('b')
        count += 1
        blockedList = blockedList + [insert]
    else:
        for index in range(len(blockedList)-1):
            if insert[0] > blockedList[index][1] and insert[1] < blockedList[index+1][0] :
                blockedList = blockedList[:index+1] + [insert] + blockedList[index+1:]
                print('c')
                count += 1
                break

        for index in range(len(blockedList)):
            if insert[0] <= blockedList[index][1] and insert[1] >= blockedList[index][1]:
                print('d')
                count += 1
                blockedList[index][1] = insert[1]
                break
        
        for index in range(len(blockedList)):
            if insert[0] <= blockedList[index][0] and insert[1] >= blockedList[index][0]:
                print('e')
                count += 1
                blockedList[index][0] = insert[0]
                break
                

    print(blockedList)
    return [blockedList, count]

print(blocked)
# blocked = insertRange(blocked, [25, 60])
[blocked, count] = insertRange(blocked, [3863319608, 3871068145], count)
[blocked, count] = insertRange(blocked, [881357481, 892360003], count)
[blocked, count] = insertRange(blocked, [1109987968, 1119969449], count)
[blocked, count] = insertRange(blocked, [3658860150, 3317364128], count)
[blocked, count] = insertRange(blocked, [3315323905, 4213558177], count)


print(count)
# blocked = insertRange(blocked, [0, 3])
# blocked = insertRange(blocked, [100, 300])
# blocked = insertRange(blocked, [20, 25])
