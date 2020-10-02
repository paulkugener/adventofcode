#! python3

# --- Puzzle input = Boss stats
# Hit Points: 103
# Damage: 9
# Armor: 2
BOSS_HP = 103
BOSS_DMG = 9
BOSS_ARMOR = 2

# Player
PLAYER_HP = 100

# --- Shop:
# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3

# --- Rules:
# - the player MUST buy 1 weapon
weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
# - the player CAN buy 0-1 armor
armors = [(0,0,0), (13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
# - the player CAN buy 0-2 rings
    # 0, 1, 2, 3, 4, 5, 6
    # 12, 13, 14, 15, 16
    # 23, 24, 25, 26
    # 34, 35, 36
    # 45, 46
    # 56
rings = [(0,0,0), (25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3),
         (75,3,0), (125,4,0), (45,1,1), (65,1,2), (105,1,3),
         (150,5,0), (70,2,1), (90,2,2), (130,2,3),
         (120,3,1), (140,3,2), (180,3,3),
         (60,0,3), (100,0,4),
         (120,0,5)
        ]

result1 = 500
result2 = 0

# simulate fight for each configuration
for w in weapons:
    for a in armors:
        for r in rings:
            inventory_cost = w[0] + a[0] + r[0]
            player_dmg = w[1] + a[1] + r[1]
            player_armor = w[2] + a[2] + r[2]

            # init HP
            player_hp = PLAYER_HP
            boss_hp = BOSS_HP
            # fight until someone dies
            next_move = "player"
            while player_hp > 0 and boss_hp > 0:
                if next_move == "player":
                    boss_hp -= max(1, player_dmg - BOSS_ARMOR)
                    next_move = "boss"
                else:
                    player_hp -= max(1, BOSS_DMG - player_armor)
                    next_move = "player"

            # print("\n", inventory_cost, w, a, r)
            # print("player:", "hp", player_hp, ", dmg", player_dmg, ", armor", player_armor)
            # print("boss:", "hp", boss_hp, ", dmg", BOSS_DMG, ", armor", BOSS_ARMOR)

            if player_hp > 0:
                if inventory_cost < result1:
                    result1 = inventory_cost
            else:
                if inventory_cost > result2:
                    result2 = inventory_cost

print(result1)
print(result2)
