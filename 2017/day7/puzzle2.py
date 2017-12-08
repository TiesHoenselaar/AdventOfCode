# with open("input.txt") as f:
with open("testInput.txt") as f:
	content = f.readlines()
content = [x.split() for x in content]

bottom = 'cyrupz'
names = []
leaves = []
for i in range(len(content)):
	current = content[i]
	if len(current) == 2:
		names.append([current[0], int(current[1][1:-1])])
	else:
		leaves.append([current[0], int(current[1][1:-1])])

print(names)
print(leaves)