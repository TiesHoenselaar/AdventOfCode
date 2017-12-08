with open("input.txt") as f:
# with open("inputTest.txt") as f:
	content = f.readlines()
content = [x.split() for x in content]

variables = []
maxValue = 0

for i in range(len(content)):
	if content[i][0] not in variables:
		variables.append(content[i][0])
		globals()[content[i][0]] = 0

for i in range(len(content)):
	instruction = content[i]
	plusMinus = instruction[1]
	conditionSign = instruction[5]

	if conditionSign == '<':
		if globals()[instruction[4]] < int(instruction[6]):
			if plusMinus == 'inc':
				globals()[instruction[0]] += int(instruction[2])
			elif plusMinus == 'dec':
				globals()[instruction[0]] -= int(instruction[2])

	if conditionSign == '>':
		if globals()[instruction[4]] > int(instruction[6]):
			if plusMinus == 'inc':
				globals()[instruction[0]] += int(instruction[2])
			elif plusMinus == 'dec':
				globals()[instruction[0]] -= int(instruction[2])

	if conditionSign == '<=':
		if globals()[instruction[4]] <= int(instruction[6]):
			if plusMinus == 'inc':
				globals()[instruction[0]] += int(instruction[2])
			elif plusMinus == 'dec':
				globals()[instruction[0]] -= int(instruction[2])

	if conditionSign == '>=':
		if globals()[instruction[4]] >= int(instruction[6]):
			if plusMinus == 'inc':
				globals()[instruction[0]] += int(instruction[2])
			elif plusMinus == 'dec':
				globals()[instruction[0]] -= int(instruction[2])

	if conditionSign == '==':
		if globals()[instruction[4]] == int(instruction[6]):
			if plusMinus == 'inc':
				globals()[instruction[0]] += int(instruction[2])
			elif plusMinus == 'dec':
				globals()[instruction[0]] -= int(instruction[2])

	if conditionSign == '!=':
		if globals()[instruction[4]] != int(instruction[6]):
			if plusMinus == 'inc':
				globals()[instruction[0]] += int(instruction[2])
			elif plusMinus == 'dec':
				globals()[instruction[0]] -= int(instruction[2])

	variablesValues = []
	for j in range(len(variables)):
		variablesValues.append(globals()[variables[j]])
	
	currentMaxValue = max(variablesValues)
	if currentMaxValue > maxValue:
		maxValue = currentMaxValue
	

print(maxValue)
