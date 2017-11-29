def int2bin(i):
    if i == 0: return "0"
    s = ''
    count_1 = 0
    while i:
        if i & 1 == 1:
            s = "1" + s
            count_1 += 1
        else:
            s = "0" + s
        i /= 2
    return s,count_1

input = 1358

size = 100

startpointX = 1
startpointY = 1

endpointX = 31
endpointY = 39


grid = []
for i in range(size):
	grid.append([])

for x in range(size):
	for y in range(size):
		num1 = x*x + 3*x + 2*x*y + y + y*y + 10
		# num2 = int2bin(num1)
		num1Bin,numberOfOnes = int2bin(num1)

		if numberOfOnes % 2 == 0: # even
			grid[x].append('0,')
		else:
			grid[x].append('1,')

def printMaze(grid):
	for i in range(len(grid)):
		line = ''
		for j in range(len(grid[i])):
			if j == startpointX and i == startpointY:
				line += 'S,'
			elif j == endpointX and i == endpointY:
				line += 'E,'
			else:
				line += grid[j][i]
		print(line)

printMaze(grid)
