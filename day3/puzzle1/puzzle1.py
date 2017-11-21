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

for j in range(len(content)):
	results = [int(i) for i in content[j]]
	# print(results)
	# print(testTriangle(results))
	count += testTriangle(results)

print(count)
