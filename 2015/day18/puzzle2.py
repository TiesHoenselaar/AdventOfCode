import numpy as np

fname = "day18/input2.txt"
with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]

lights = []

for row in range(len(content)):
    lights.append([x=="#" for x in content[row]])
# print(*lights, sep = "\n")

size = len(content)
steps = 100
for i in range(steps):

    new_lights = [[[0] for i in range(size)] for i in range(size)]

    for row in range(len(lights)):
        for col in range(len(lights)):
            total = 0
            for d_row in range(-1, 2):
                for d_col in range(-1, 2):
                    if row+d_row >= 0 and row+d_row < size and col+d_col >= 0 and col+d_col < size:
                        if not (d_row == 0 and d_col == 0):
                            if lights[row+d_row][col+d_col] == 1:
                                total += 1   
            if lights[row][col] == 1:
                if total == 2 or total == 3:
                    new_lights[row][col] = 1
                else:
                    new_lights[row][col] = 0

            else:
                if total == 3:
                    new_lights[row][col] = 1
                else:
                    new_lights[row][col] = 0
    new_lights[0][0] = 1
    new_lights[size-1][0] = 1
    new_lights[0][size-1] = 1
    new_lights[size-1][size-1] = 1

    lights = new_lights

    # print(*lights, sep = "\n")

print(sum(sum(lights, [])))