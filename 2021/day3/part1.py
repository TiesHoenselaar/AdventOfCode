with open('input.txt', 'r') as f:
    lines = f.readlines()

number_length = len(lines[0]) - 1
print(number_length)

count_0 = number_length * [0]
count_1 = number_length * [0]

for line in lines:
    for i in range(number_length):
        if line[i] == '0':
            count_0[i] += 1
        else:
            count_1[i] += 1

print(count_0)
print(count_1)

gamma_rate = ''
epsilon_rate = ''

for j in range(number_length):
    if count_0[j] > count_1[j]:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

print(gamma_rate)
print(epsilon_rate)

gamma_rate_decimal = 0
epsilon_rate_decimal = 0
for k in range(number_length):
    gamma_rate_decimal += int(gamma_rate[-k-1]) * 2 ** k
    epsilon_rate_decimal += int(epsilon_rate[-k-1]) * 2 ** k

print(gamma_rate_decimal)
print(epsilon_rate_decimal)

power_consumtion = gamma_rate_decimal * epsilon_rate_decimal

print('power_consumtion:', power_consumtion)

# 12040320 too high
