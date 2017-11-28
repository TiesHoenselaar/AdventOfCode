# with open("testInput.txt") as f:
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


def botNumber(string):
	botNum = 0
	bots = []
	if string.split(' ')[0] == 'value':
		botNum = int(string.split(' ')[5])
	if string.split(' ')[0] == 'bot':
		stringSplitted = string.split(' ')
		for i in range(len(stringSplitted)):
			if stringSplitted[i] == 'bot':
				bots.append(int(stringSplitted[i+1]))
		botNum = max(bots)
	return botNum

maxBotNumber = 0
for i in range(len(content)):
	if botNumber(content[i]) > maxBotNumber:
		maxBotNumber = botNumber(content[i])

# print(maxBotNumber) ### 209

botChoices = []
storage = []
for i in range(maxBotNumber+1):
	botChoices.append([-1, -1])
	storage.append([])

## initialize botChoices and storage
for i in range(len(content)):
	stringSplitted = content[i].split(' ')
	if stringSplitted[0] == 'bot':
		if stringSplitted[5] == 'bot':
			botChoices[int(stringSplitted[1])][0] = int(stringSplitted[6])
		elif stringSplitted[5] == 'output':
			botChoices[int(stringSplitted[1])][0] = -1-int(stringSplitted[6])

		if stringSplitted[10] == 'bot':
			botChoices[int(stringSplitted[1])][1] = int(stringSplitted[11])
		elif stringSplitted[10] == 'output':
			botChoices[int(stringSplitted[1])][1] = -1-int(stringSplitted[11])
	elif stringSplitted[0] == 'value':
		storage[int(stringSplitted[5])].append(int(stringSplitted[1]))

output = []
numOutputs = -min(min(botChoices))
for j in range(numOutputs):
	output.append([])

def loopOnce():
	for bot in range(len(storage)):
		if len(storage[bot]) > 1:
			if storage[bot] == [61, 17] or storage[bot] == [17, 61]:
				print('puzzle 1:', bot)
			minValue = min(storage[bot])
			maxValue = max(storage[bot])

			if botChoices[bot][0] < 0:
				output[-botChoices[bot][0]-1].append(minValue)
			else:
				storage[botChoices[bot][0]].append(minValue)

			if botChoices[bot][1] < 0:
				output[-botChoices[bot][1]-1].append(maxValue)
			else:
				storage[botChoices[bot][1]].append(maxValue)

			storage[bot] = []




while max(storage) != []:
	loopOnce()

print('puzzle 2:', output[0][0]*output[1][0]*output[2][0])