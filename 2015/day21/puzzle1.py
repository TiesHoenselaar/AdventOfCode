from collections import namedtuple


Item = namedtuple('Item', ['name', 'cost', 'dmg', 'armor'])

WEAPONS = [
    Item('Dagger',      8,      4,      0),
    Item('Shortsword',  10,     5,      0),
    Item('Warhammer',   25,     6,      0),
    Item('Longsword',   40,     7,      0),
    Item('Greataxe',    74,     8,      0)
]

ARMOR = [
    Item('Nothing',     0,      0,      0),
    Item('Leather',     13,     0,      1),
    Item('Chainmail',   31,     0,      2),
    Item('Splintmail',  53,     0,      3),
    Item('Bandedmail',  75,     0,      4),
    Item('Platemail',   102,    0,      5)
]

RINGS = [
    Item('Nothing 1',   0,      0,      0),
    Item('Nothing 2',   0,      0,      0),
    Item('Damage +1',   25,     1,      0),
    Item('Damage +2',   50,     2,      0),
    Item('Damage +3',   100,    3,      0),
    Item('Defense +1',  20,     0,      1),
    Item('Defense +2',  40,     0,      2),
    Item('Defense +3',  80,     0,      3)
]


def player_wins(player_hitpoints, player_dmg, player_armor,
                boss_hitpoints, boss_dmg, boss_armor):
    
    player_hits = player_dmg - boss_armor
    if player_hits < 1:
        player_hits = 1

    boss_hits = boss_dmg - player_armor
    if boss_hits < 1:
        boss_hits = 1

    n, remainder = divmod(boss_hitpoints, player_hits)
    if remainder == 0:
        n -= 1

    if boss_hits * n >= player_hitpoints:
        return False
    return True

BOSS_HITPOINTS = 103
BOSS_DMG = 9
BOSS_ARMOR = 2

minimum_cost = 99999
maximum_cost = 0

for w in WEAPONS:
    for a in ARMOR:
        for r1 in RINGS:
            for r2 in RINGS:
                
                if r1.name == r2.name:
                    continue

                player_hitpoints = 100
                player_dmg = w.dmg + r1.dmg + r2.dmg
                player_armor = a.armor + r1.armor + r2.armor
                player_cost = w.cost + a.cost + r1.cost + r2.cost

                if player_wins(player_hitpoints, player_dmg, player_armor, BOSS_HITPOINTS, BOSS_DMG, BOSS_ARMOR):
                    minimum_cost = min(player_cost, minimum_cost)
                else:
                    maximum_cost = max(player_cost, maximum_cost)

print(minimum_cost)
print(maximum_cost)
