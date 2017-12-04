with open("input.txt") as f:
    content = f.readlines()[0]

## puzzle 1

counter = 0
for i in range(len(content)-1):
    if content[i] == content[i+1]:
        counter += int(content[i])

if content[0] == content[-1]:
    counter += int(content[0])


print(counter)

## puzzle 2

counter2 = 0
listLength = len(content)

for i in range(len(content)):
    if content[i] == content[(i+listLength/2)%listLength]:
        counter2 += int(content[i])

print(counter2)