# Dog Years

dog_year = 0
human_year = float(input('enter human years: '))

if human_year < 0:
    print("years can't be negative")
elif human_year <= 2:
    dog_year = human_year * 10.5
    print('correspond to', dog_year, 'dog years')
else:
    dog_year = 2 * 10.5 + (human_year - 2) * 4
    print('correspond to', dog_year, 'dog years')

