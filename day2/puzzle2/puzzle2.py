allowedPositions = [[0,2],[-1,1],[0,1],[1,1],[-2,0],[-1,0],[0,0],[1,0],[2,0],[-1,-1],[0,-1],[1,-1],[0,-2]]

def updatePos(pos,code):
    if code == "U":
        new_pos = [pos[0], pos[1] + 1]
    elif code == "R":
        new_pos = [pos[0] + 1, pos[1]]
    elif code == "D":
        new_pos = [pos[0], pos[1] - 1]
    elif code == "L":
        new_pos = [pos[0] - 1, pos[1]]

    if new_pos in allowedPositions:
        return new_pos
    else:
        return pos

def posToNum(pos):  ## So dirty :(
    if pos == [0,2]: return 1
    if pos == [-1,1]: return 2
    if pos == [0,1]: return 3
    if pos == [1,1]: return 4
    if pos == [-2,0]: return 5
    if pos == [-1,0]: return 6
    if pos == [0,0]: return 7
    if pos == [1,0]: return 8
    if pos == [2,0]: return 9
    if pos == [-1,-1]: return "A"
    if pos == [0,-1]: return "B"
    if pos == [1,-1]: return "C"
    if pos == [0,-2]: return "D"
    else: return "error"

with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

pos = [0, 0]

for i in range(len(content)):
    code = content[i]
    for j in range(len(code)):
        pos = updatePos(pos,code[j])

    print(posToNum(pos))
