def calc_cost(start_pos, end_pos):

    steps = abs(end_pos - start_pos)

    

    if steps % 2 == 0: # even
        return steps*(steps + 1)/2

    else: # odd
        return (steps + 1) * (steps // 2) + (steps+1)/2


with open ('input.txt') as f:
    positions = [int(x) for x in f.read().split(',')]


min_pos = min(positions)
max_pos = max(positions)

print(min_pos, max_pos)

def calc_fuel(positions, final_pos):
    cost = 0
    for p in positions:
        cost += calc_cost(p, final_pos)
        
    return cost

cost = 9999999999999999999
for pos in range(min_pos, max_pos):
    
    new_cost = calc_fuel(positions, pos)
    
    if new_cost < cost:
        cost = new_cost

print(int(cost))
