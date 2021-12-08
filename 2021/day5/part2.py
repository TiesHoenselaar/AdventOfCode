with open('input.txt', 'r') as f:
    input_lines = f.read().splitlines()

#input_lines = ['9,7 -> 7,9']
#input_lines = ['7,9 -> 9,7']
#input_lines = ['1,1 -> 3,3']
#input_lines = ['3,3 -> 1,1']


#print(input_lines)

min_x = 99999999999
max_x = -1
min_y = 99999999999
max_y = -1

lines = []
for line in input_lines:
    line = line.replace(' -> ', ',')

    line = [int(x) for x in line.split(',')]
    if line[0] < min_x: min_x = line[0]
    if line[2] < min_x: min_x = line[2]
    if line[0] > max_x: max_x = line[0]
    if line[2] > max_x: max_x = line[2]

    if line[1] < min_y: min_y = line[1]
    if line[3] < min_y: min_y = line[3]
    if line[1] > max_y: max_y = line[1]
    if line[3] > max_y: max_y = line[3]

    
    lines.append(line)

diagram = [[0 for x in range(max_y+1)] for y in range(max_x+1)]


for line in lines:
    #print(line)
    [x1, y1, x2, y2] = line

    #print("x1:",x1,"y1:",y1,"x2:",x2,"y2:",y2)

    if x1 == x2:
        if y2 > y1:
            for y in range(y1, y2+1):
                diagram[x1][y] += 1
        else:
            for y in range(y2, y1+1):
                diagram[x1][y] += 1

    elif y1 == y2:
        if x2 > x1:
            for x in range(x1, x2+1):
                diagram[x][y1] += 1
        else:
            for x in range(x2, x1+1):
                diagram[x][y1] += 1

    else:
        c = 0
        if x2 > x1:
            if y2 > y1:
                for x in range(x1, x2+1):
                    diagram[x][y1+c] += 1
                    c += 1
            else:
                for x in range(x1, x2+1):
                    diagram[x][y1-c] += 1
                    c += 1
        else:
            if y2 > y1:
                for x in range(x2, x1+1):
                    diagram[x][y2-c] += 1
                    c += 1
            else:
                for x in range(x2, x1+1):
                    diagram[x][y2+c] += 1
                    c += 1

count = 0
for x in range(max_x+1):
    for y in range(max_y+1):
        if diagram[x][y] >= 2:
            count += 1

print(count)

