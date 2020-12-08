# What Color Is That Square?

position = input('enter a chess position: ')
col = position[0]
row = int(position[1])

color_temp = -1  # 1=black / 2=white / -1=error
if col == 'a' or col == 'c' or col == 'e' or col == 'g':
    color_temp = 1
elif col == 'b' or col == 'd' or col == 'f' or col == 'h':
    color_temp = 2

if color_temp == -1 or row > 8 or row < 1:
    print('position not valid')
else:
    color_temp = color_temp + row
    if color_temp % 2 == 0:
        color = 'black'
    else:
        color = 'white'

    print('the square is', color)
