with open("input.txt") as f:
    content = f.readlines()
content = [x.split() for x in content]

counter = 0

for i in range(len(content)):
	words = [content[i][0]]
	passphrase = True
	for j in range(len(content[i])-1):
		if content[i][j+1] not in words:
			words.append(content[i][j+1])
		else:
			passphrase = False
			break
	if passphrase:
		counter += 1

print(counter)

counter2 = 0
for i in range(len(content)):
	words = [''.join(sorted(content[i][0]))]
	print(words)
	passphrase = True
	for j in range(len(content[i])-1):
		if ''.join(sorted(content[i][j+1])) not in words:
			words.append(''.join(sorted(content[i][j+1])))
		else:
			passphrase = False
			break
	if passphrase:
		counter2 += 1

print(counter2)