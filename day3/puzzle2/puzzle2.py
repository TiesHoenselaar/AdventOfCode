# read input
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip().split() for x in content]

count = 0

def testTriangle(results):
	
	checks = [0, 0, 0]
	
	if results[0] + results[1] > results[2]: checks[0] = 1
	if results[1] + results[2] > results[0]: checks[1] = 1
	if results[0] + results[2] > results[1]: checks[2] = 1

	if sum(checks) == 3:
		return 1
	else: return 0

for k in range(3):
	for j in range(len(content)/3):
		results1 = [int(i) for i in content[j*3]]
		results2 = [int(i) for i in content[j*3+1]]
		results3 = [int(i) for i in content[j*3+2]]
		
		contents = [results1[k], results2[k], results3[k]]
		
		count += testTriangle(contents)

print(count)
