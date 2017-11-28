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

print(maxBotNumber) ### 209

botChoices = []

for i in range(maxBotNumber):
	botChoices.append([-1, -1])