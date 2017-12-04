x = 0
y = 0

heading = 0

headings_x = [0, 1, 0, -1]
headings_y = [1, 0, -1, 0]

def printCoordinates(x,y):
    print("x={0},y={1}".format(x, y))
    return

def calculateCoordinates(x_init, y_init, heading, forward):
    x = x_init + headings_x[heading] * forward
    y = y_init + headings_y[heading] * forward
    return [x,y]


def calculateHeading(head_init, lor):
    if lor == "L":
        heading = (head_init-1)%4
    elif lor == "R":
        heading = (head_init+1)%4
    return heading

f = open("input.txt")

commands = [word.strip() for line in f.readlines() for word in line.split(',') if word.strip()]
## print(", ".join(commands))

coordinatesVisited = []
doubleVisited = 0

i = 0
while i < len(commands) and doubleVisited == 0:
    command = commands[i]
    input_1 = command[0]
    input_2 = int(command[1:])

        

    heading = calculateHeading(heading, input_1)

    for j in range(input_2):
        if doubleVisited == 0:
            [x,y] = calculateCoordinates(x,y,heading,1)
            #printCoordinates(x,y)
            if [x,y] in coordinatesVisited:
                doubleVisited = 1
        
            coordinatesVisited.append([x,y])
    i += 1

## printCoordinates(x,y)

dist = (x**2+y**2)**0.5
print("Distance = {0}".format(x+y))
