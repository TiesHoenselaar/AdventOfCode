with open('input.txt', 'r') as f:
    input_lines = f.read().splitlines()

#input_lines = ['9,7 -> 7,7']

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

#print(lines)
print(min_x, min_y, max_x, max_y)

diagram = [[0 for x in range(max_y+1)] for y in range(max_x+1)]


for line in lines:
    #print(line)
    [x1, y1, x2, y2] = line

    #print("x1:",x1,"y1:",y1,"x2:",x2,"y2:",y2)

    if x1 == x2:
        if y2 > y1:
            for y in range(y1, y2+1):
            
                diagram[x1][y] += 1
                #print(x1, y)
        else:
            for y in range(y2, y1+1):
                diagram[x1][y] += 1
                #print(x1, y)

    if y1 == y2:
        if x2 > x1:
            for x in range(x1, x2+1):
                diagram[x][y1] += 1
                #print(x, y1)
        else:
            for x in range(x2, x1+1):
                diagram[x][y1] += 1
                #print(x, y1)

count = 0
for x in range(max_x+1):
    for y in range(max_y+1):
        if diagram[x][y] >= 2:
            count += 1

print(count)

#for diagram_line in diagram:
#    print(diagram_line)

