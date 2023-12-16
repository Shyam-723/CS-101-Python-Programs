months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
rain = []
for x in :
    rainfall = int(input(f'Input the amount of rain on {x} : '))
    rain.append(rainfall)
    

total = sum(rain)
avg = total/12
min_rain = min(rain)
max_rain = max(rain)


print(f'The total rain that fell is {total} ml')
print(f'The average rain that fell permonth is {avg} ml')
print(f'The month with the maximum rain is month {max_rain}')
print(f'The month with the minimum rain is month {min_rain}')
        
