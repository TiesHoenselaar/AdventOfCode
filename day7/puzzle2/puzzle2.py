def testABA(string, BAB):
	for i in range(len(string)-2):
		if string[i] == string[i+2] and string[i] != string[i+1]:
			BAB.append(string[i+1]+string[i]+string[i+1])
		i += 1
	return BAB

def testBAB(string, BAB):
	for i in range(len(string)-2):
		if string[i] == string[i+2] and string[i] != string[i+1]:
			BAB.append(string[i]+string[i+1]+string[i+2])
		i += 1
	return BAB

with open("input.txt") as f:
    content = f.readlines()
content = [x.strip().replace('[',',').replace(']',',').split(',') for x in content]

globalCount = 0
for j in range(len(content)):
	BABs = []
	BABs2 = []
	count = 0
	for k in range(len(content[j])):
		if k%2 == 0:
			BABs = testABA(content[j][k],BABs)
		elif k%2 == 1:
			BABs2 = testBAB(content[j][k],BABs2)
	
	for i in range(len(BABs2)):
		if BABs2[i] in BABs:
			count += 1

	if count > 0:
		globalCount += 1

print(globalCount)

