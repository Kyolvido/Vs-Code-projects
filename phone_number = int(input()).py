phone_number = 8015556314
area_code = f'({phone_number // 10000000})'
mid_three = f' -{phone_number % 10000000 // 10000}'
lower_four = f'{phone_number % 10000}'
print(area_code) 
print(lower_four)
print(mid_three)
