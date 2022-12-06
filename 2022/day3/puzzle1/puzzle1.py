input_file = "day3/puzzle1/intput.txt"
# input_file = "day3/puzzle1/test_input.txt"

total_priority = 0
with open(input_file, "r") as input_file:
    for line in input_file:
        text_line = line.strip()

        first_part = text_line[:int(len(text_line)/2)]
        second_part = text_line[int(len(text_line)/2):]
        # print(text_line, first_part, second_part)

        for letter in first_part:
            if letter in second_part:
                if letter.islower():
                    priority = ord(letter) - 96
                else:
                    priority = ord(letter) - 64 + 26
                total_priority += priority
                break

print(total_priority)