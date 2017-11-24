lstLength = 3
screen = [[0,0,0,0,0,0,0] for _ in range(lstLength)]

def printScreen(screen):
	for i in range(len(screen)):
		print(screen[i])
	print('\n')

def createRectangle(screen,x,y):
	for i in range(y):
		for j in range(x):
			screen[i][j] = 1
	return screen


printScreen(screen)
screen = createRectangle(screen,3,2)
printScreen(screen)