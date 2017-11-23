testString = "abba[mnop]qrst"

def testABA(string):
	ABA = 0
	for i in range(len(string)-2):
		if string[i] == string[i+2] and string[i] != string[i+1]:
			ABA = 1
		i += 1
	return ABA

def testBAB(string):
	BAB = 0
	for i in range(len(string)-2):
		if string[i] == string[i+2] and string[i] != string[i+1]:
			BAB = 1
		i += 1
	return ABA

def testTSL(IP):
	if (testABBA(IP[0]) or testABBA(IP[2])) and not testABBA(IP[1]):
		return 1
	else:
		return 0

with open("input.txt") as f:
    content = f.readlines()
content = [x.strip().replace('[',',').replace(']',',').split(',') for x in content]

count = 0
for j in range(len(content)):
	sum1 = 0
	sum2 = 0
	for k in range(len(content[j])):
		if k%2 == 0:
			sum1 += testABBA(content[j][k])
		elif k%2 == 1:
			sum2 += testABBA(content[j][k])
	
	if sum1 >= 1 and sum2 == 0:
		count += 1

print(count)