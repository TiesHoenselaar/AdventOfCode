with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

number_length = len(lines[0])
numbers = []
numbers2 = []
for line in lines:
  numbers.append(line)
  numbers2.append(line)

for i in range(number_length):
# for i in range(1):
    numbers_0 = []
    numbers_1 = []
    for j in range(len(numbers)):
        if numbers[j][i] == '0':
            numbers_0.append(numbers[j])
        else:
            numbers_1.append(numbers[j])

    if len(numbers_1) >= len(numbers_0):
        numbers = numbers_1
    else:
        numbers = numbers_0

    if len(numbers) == 1:
        break

oxygen_generator_rating = numbers[0]

for i in range(number_length):
    numbers_0 = []
    numbers_1 = []
    for j in range(len(numbers2)):
        if numbers2[j][i] == '0':
            numbers_0.append(numbers2[j])
        else:
            numbers_1.append(numbers2[j])


    if len(numbers_0) <= len(numbers_1):
        numbers2 = numbers_0
    else:
        numbers2 = numbers_1

    if len(numbers2) == 1:
        break

CO2_scrubber_rating = numbers2[0]



oxygen_generator_rating_decimal = 0
CO2_scrubber_rating_decimal = 0
for k in range(number_length):
    oxygen_generator_rating_decimal += int(oxygen_generator_rating[-k-1]) * 2 ** k
    CO2_scrubber_rating_decimal += int(CO2_scrubber_rating[-k-1]) * 2 ** k

# print(oxygen_generator_rating_decimal)
# print(CO2_scrubber_rating_decimal)

life_support_rating = oxygen_generator_rating_decimal * CO2_scrubber_rating_decimal

print('life_support_rating:', life_support_rating)
