#! python3
from itertools import product
import sys

# --- Puzzle input = Boss stats
# Hit Points: 58
# Damage: 9

BOSS_HP = 58
BOSS_DMG = 9

# Player
PLAYER_HP = 50
PLAYER_MANA = 500

# --- Spells:
# [M] Magic Missile (53 mana). It instantly does 4 damage.
# [D] Drain (73 mana). It instantly does 2 damage and heals you for 2 hit points.
# [S] Shield (113 mana). It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# [P] Poison (173 mana). It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# [R] Recharge (229 mana). It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
spells = 'MDSPR'


result = 100000
part2 = True

for actions in range(9, 10): # for the range I just increased the values until the player was able to win VS the boss
    print("number of actions", actions)
    all_spell_orders = product(spells, repeat=actions)
    actions += 1
    for spell_order in all_spell_orders:
        # this is one fight
        #print(spell_order)
        # init
        player_hp = PLAYER_HP
        player_mana = PLAYER_MANA
        player_mana_spend = 0
        boss_hp = BOSS_HP
        # effects
        buff_shield = 0
        buff_recharge = 0
        debuff_poison = 0

        next_move = "player"
        player_move = 0
        while player_hp > 0 and boss_hp > 0 and player_mana >= 0:
            #print(next_move)
            #print(player_hp, player_mana)
            #print(boss_hp)
            player_armor = 0
            # effects are happening every turn (player & boss)
            if buff_shield > 0:
                player_armor = 7
                buff_shield -= 1
            if debuff_poison > 0:
                boss_hp -= 3
                debuff_poison -= 1
                if boss_hp <= 0: # check if the boss is dead
                    break
            if buff_recharge > 0:
                player_mana += 101
                buff_recharge -= 1

            if next_move == "player":
                # player turn
                if part2:
                    player_hp -= 1
                    if player_hp <= 0: # check if the player is dead
                        break
                # spell
                if player_move > len(spell_order)-1:
                    break
                spell = spell_order[player_move]
                if spell == "M":
                    player_mana -= 53
                    player_mana_spend += 53
                    boss_hp -= 4
                elif spell == "D":
                    player_mana -= 73
                    player_mana_spend += 73
                    boss_hp -= 2
                    player_hp += 2
                elif spell == "S":
                    player_mana -= 113
                    player_mana_spend += 113
                    buff_shield = 6
                elif spell == "P":
                    player_mana -= 173
                    player_mana_spend += 173
                    debuff_poison = 6
                elif spell == "R":
                    player_mana -= 229
                    player_mana_spend += 229
                    buff_recharge = 5

                next_move = "boss"
                player_move += 1
            else: 
                # boss turn
                player_hp -= max(1, BOSS_DMG - player_armor)
                next_move = "player"

        if boss_hp <= 0:
            #print("player wins: player hp =", player_hp, ", boss hp =", boss_hp)
            if player_mana_spend < result:
                print(player_mana_spend)
                result = player_mana_spend
        else:
            pass
            #print("boss wins: player hp =", player_hp, ", boss hp =", boss_hp)

print(result)
