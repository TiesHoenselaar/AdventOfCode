with open('input.txt', 'r') as f:
    lines = f.readlines()

count = 0
previous_measurement = int(lines[0]) + int(lines[1]) + int(lines[2])
for i in range(len(lines) - 3):
    current_measurement = int(lines[i+1]) + int(lines[i+2]) + int(lines[i+3])
    
    if current_measurement > previous_measurement:
        count += 1
    previous_measurement = current_measurement

print(count)
