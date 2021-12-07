with open ('input.txt', 'r') as f:
    lines = f.readlines()

horizontal = 0
depth = 0
for line in lines:
    command, value = line.split(' ')

    if command == 'forward':
        horizontal += int(value)

    if command == 'down':
        depth += int(value)

    if command == 'up':
        depth -= int(value)
        

print('horizontal:', horizontal, 'depth:', depth)
print('horizontal * vertical =', horizontal*depth)
