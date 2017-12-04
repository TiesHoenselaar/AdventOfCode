inputNumber = 289326

# Right Up Left Down

initPos = [0,0]

grid = [1,initPos]

def moveRight(gridPos):
	[start_i, [startX, startY]] = gridPos
	return [start_i+1,[startX+1,startY]]

def moveUp(gridPos):
	[start_i, [startX, startY]] = gridPos
	return [start_i+1,[startX,startY+1]]

def moveLeft(gridPos):
	[start_i, [startX, startY]] = gridPos
	return [start_i+1,[startX-1,startY]]

def moveDown(gridPos):
	[start_i, [startX, startY]] = gridPos
	return [start_i+1,[startX,startY-1]]

grid.append(moveRight(grid))
grid.append(moveUp(grid[-1]))

counter = 2

i = 0
while i < inputNumber:
	for j in range(counter):
		grid.append(moveLeft(grid[-1]))
		i += 1
	for j in range(counter):
		grid.append(moveDown(grid[-1]))
		i += 1
	counter += 1
	for j in range(counter):
		grid.append(moveRight(grid[-1]))
		i += 1
	for j in range(counter):
		grid.append(moveUp(grid[-1]))
		i += 1
	counter += 1


finalPosition = grid[inputNumber][1]

print(abs(finalPosition[0])+abs(finalPosition[1]))
