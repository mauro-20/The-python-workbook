# Faces onMoney

# George Washington $1
# Thomas Jefferson $2
# Abraham Lincoln $5
# Alexander Hamilton $10
# Andrew Jackson $20
# Ulysses S. Grant $50
# Benjamin Franklin $100

banknote = int(input('enter a banknote size: '))

face = ''
if banknote == 1:
    face = 'George Washington'
elif banknote == 2:
    face = 'Thomas Jefferson'
elif banknote == 5:
    face = 'Abraham Lincoln'
elif banknote == 10:
    face = 'Alexander Hamilton'
elif banknote == 20:
    face = 'Andrew Jackson'
elif banknote == 50:
    face = 'Ulysses S. Grant'
elif banknote == 100:
    face = 'Benjamin Franklin'

if face == '':
    print("it doesn't exist a banknote of", banknote, "$")
else:
    print(banknote, "$ banknote has", face, "on it")
