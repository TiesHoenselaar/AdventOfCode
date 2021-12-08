with open('input.txt', 'r') as f:
    input_lines = [int(x) for x in f.read().split(',')]

fishes = input_lines
days = 80

for day in range(days):
    new_fishes = []
    new_born_fishes = []
    for i in range(len(fishes)):
        if fishes[i] > 0:
            new_fishes.append(fishes[i]-1)
        else:
            new_fishes.append(6)
            new_born_fishes.append(8)

    fishes = new_fishes + new_born_fishes

    #print(fishes)

print(len(fishes))
