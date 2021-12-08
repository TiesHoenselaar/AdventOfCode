with open ('input.txt') as f:
    lines = f.read().splitlines()

#print(lines)

count = 0
for line in lines:
    codes = line.split(' ')
    output_values = codes[-4:]
    for output_value in output_values:
        if len(output_value) in [2, 3, 4, 7]:
            count += 1

print(count)
