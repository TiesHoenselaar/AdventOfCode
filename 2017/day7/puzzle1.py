with open("input.txt") as f:
# with open("testInput.txt") as f:
	content = f.readlines()
content = [x.split() for x in content]

names = []
subnames = []

for i in range(len(content)):
	current = content[i]
	names.append(current[0])

	if len(current) > 2:
		for j in range(len(current)-3):
			if j != len(current)-4:
				subnames.append(current[j+3][0:-1])
				
			else:
				subnames.append(current[j+3])

difference = list(set(names) - set(subnames))[0]
print(difference)