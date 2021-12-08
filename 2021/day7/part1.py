with open ('input.txt') as f:
    positions = [int(x) for x in f.read().split(',')]

#print(positions)

min_pos = min(positions)
max_pos = max(positions)

print(min_pos, max_pos)

def calc_fuel(positions, final_pos):
    cost = 0
    for p in positions:
        cost += abs(p-final_pos)
        
    return cost

cost = 9999999999999999999
for pos in range(min_pos, max_pos):
    
    new_cost = calc_fuel(positions, pos)
    
    if new_cost < cost:
        cost = new_cost

print(cost)    


