with open ('input.txt', 'r') as f:
    lines = f.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    command, value = line.split(' ')

    if command == 'forward':
        horizontal += int(value)
        depth += (aim * int(value))

    if command == 'down':
        aim += int(value)

    if command == 'up':
        aim -= int(value)

    # print('horizontal:', horizontal, 'depth:', depth, 'aim:', aim)
        

print('horizontal:', horizontal, 'depth:', depth, 'aim:', aim)
print('horizontal * vertical =', horizontal*depth)
