with open("input.txt") as f:
	content = f.readlines()
content = [x.split() for x in content]

variables = []


for i in range(len(content)):
	if content[i][0] not in variables:
		variables.append(content[i][0])
		globals()[content[i][0]] = 0


print(variables)
