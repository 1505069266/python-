# 字典来替代switch

# switch (day)
# {
#     case 0:
#         dayName = 'sunday'
#         break
#     case 1:
#         dayName = 'monday'
#         break
#     case 2:
#         dayName = 'Tuesday'
#         break
# }

day = 0
# 利用字典的key是唯一的特性来做switch  get方法来做判断
switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday'
}

day_name = switcher.get(day, 'Unknown')

print(day_name)

