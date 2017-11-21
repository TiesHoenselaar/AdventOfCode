# read input
with open("input.txt") as f:
    content = f.readlines()
content = [x.strip().split() for x in content]

results = [int(i) for i in content[0]]
min_index = (results.index(min(results)))

indexes = [0, 1, 2]

del indexes[min_index]
# new_indexes = indexes.pop(min_index)
print(indexes)

def testTriangle(lengths):
	results = [int(i) for i in content[0]]
	min_index = (results.index(min(results)))
	indexes = [0, 1, 2]
	del indexes[min_index]

	if results[indexes[0]] + results[indexes[1]] > results[min_index]:
		return 1
	else: return 0

print(testTriangle(content))
