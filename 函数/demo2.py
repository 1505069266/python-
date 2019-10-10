# R Skill1 SKill2


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2
    return damage1, damage2


damages = damage(3, 6)

print(damages)

skill1_damage, skill2_damage = damage(10, 20)

print(type(damages))

print(skill1_damage)

print(skill2_damage)

print(type(skill2_damage))

print(type(skill1_damage))