def updatePos(pos,code):
    if code == "U":
        new_pos = [pos[0], pos[1] + 1]
    elif code == "R":
        new_pos = [pos[0] + 1, pos[1]]
    elif code == "D":
        new_pos = [pos[0], pos[1] - 1]
    elif code == "L":
        new_pos = [pos[0] - 1, pos[1]]

     ## This needs to be adjusted
    if new_pos[0] <= 1 and new_pos[0] >= -1 and new_pos[1] <= 1 and new_pos[1] >= -1:
        return new_pos
    else:
        return pos

def posToNum(pos):  ## This needs to be adjusted
    num = pos[0] + 2 + 3 * ( 1 - pos[1])
    return num

with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

pos = [0, 0]  ## This needs to be adjusted

for i in range(len(content)):
    code = content[i]
    for j in range(len(code)):
        pos = updatePos(pos,code[j])

    print(posToNum(pos))
