input_file = "day3/puzzle2/intput.txt"
#input_file = "day3/puzzle2/test_input.txt"

total_priority = 0
rucksacks = []
with open(input_file, "r") as input_file:
    for line in input_file:
        text_line = line.strip()
        rucksacks.append(text_line)
        
        if len(rucksacks) == 3:
            
            #do analysis
            for letter in rucksacks[0]:
                if letter in rucksacks[1] and letter in rucksacks[2]:
                    if letter.islower():
                        priority = ord(letter) - 96
                    else:
                        priority = ord(letter) - 64 + 26
                    total_priority += priority
                    break
            
            rucksacks = []
        
            


        # for letter in first_part:
        #     if letter in second_part:
        #         if letter.islower():
        #             priority = ord(letter) - 96
        #         else:
        #             priority = ord(letter) - 64 + 26
        #         total_priority += priority
        #         break

print(total_priority)