input_file = "day6\puzzle2\input.txt"
# input_file = "day6/puzzle2/test_input.txt"

count = 0
double_character = True
with open(input_file, "r") as input_file:
    for line in input_file:
        text_line = line.strip()


        while double_character:
            characters = [x for x in text_line[count:count+14]]
            double_character = False
            for char in characters:
                if characters.count(char) > 1:
                    double_character = True
                    break

            count += 1

        

print(count+13)