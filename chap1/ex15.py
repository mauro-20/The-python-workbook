# Distance Units

ft_inch = 12
ft_yards = 0.333333
ft_miles = 0.00018939375

feet_in = float(input('enter feet value: '))

inch = feet_in*ft_inch
yards = feet_in*ft_yards
miles = feet_in*ft_miles

print(feet_in, 'feet correspond to', inch, 'inches or', yards, 'yards or', miles, 'miles')
