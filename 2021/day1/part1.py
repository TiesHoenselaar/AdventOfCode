    with open('input.txt', 'r') as f:
        lines = f.readlines()

count= 0
index = 0
previous_number = 999999999999999999999
for line in lines:
    if index == 0:
        index += 1
    else:
        index += 1
        if int(line) > previous_number:
            count += 1
            if index < 10:
                print(count, int(line), " > ", previous_number)
    previous_number = int(line)

print(count)
