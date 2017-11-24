lstLength = 6
screen = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for x in range(lstLength)]

def printScreen(screen):
	for i in range(len(screen)):
		print(screen[i])
	print('\n')

def createRectangle(screen,x,y):
	for i in range(y):
		for j in range(x):
			screen[i][j] = 1
	return screen

def shiftColumn(screen,column,amount):
	for i in range(amount):
		tempCell = screen[-1][column]
		for j in range(len(screen)-1,0,-1):
			screen[j][column] = screen[j-1][column]
		screen[0][column] = tempCell
	return screen


def shiftRow(screen, row, amount):
	for i in range(amount):
		tempCell = screen[row][-1]
		for j in range(len(screen[row])-1,0,-1):
			screen[row][j] = screen[row][j-1]
		screen[row][0] = tempCell
	return screen


# screen = createRectangle(screen,3,2)
# screen = shiftColumn(screen, 1, 1)
# screen = shiftRow(screen, 0, 4)
# screen = shiftColumn(screen, 1, 1)

with open("input.txt") as f:
    content = f.readlines()

# print(content[1][0:10])

for k in range(35):
	if content[k][0:4] == 'rect':
		size = content[k][5:-1].split('x')
		screen = createRectangle(screen,int(size[0]),int(size[1]))
	elif content[k][0:10] == 'rotate row':
		cleanedUp = (content[k][11:-1].split('='))
		information = (cleanedUp[1].split(' '))
		screen = shiftRow(screen,int(information[0]),int(information[2]))
	elif content[k][0:10] == 'rotate col':
		cleanedUp = (content[k][16:-1].split('='))
		information = (cleanedUp[1].split(' '))
		screen = shiftColumn(screen,int(information[0]),int(information[2]))

printScreen(screen)