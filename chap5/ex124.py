# Line of Best Fit

# displays the equation of the line of best fit

Xs = []
Ys = []

x = input('enter X (blank to quit): ')
while x != '':
    y = input('enter Y: ')
    Xs.append(float(x))
    Ys.append(float(y))
    x = input('enter X (blank to quit): ')

sigXY = 0
for i in range(len(Xs)):
    sigXY += Xs[i]*Ys[i]

sigX2 = 0
for i in range(len(Xs)):
    sigX2 += Xs[i]**2

x_av = sum(Xs)/len(Xs)
y_av = sum(Ys)/len(Ys)

m = (sigXY-(sum(Xs)*sum(Ys))/len(Xs)) / (sigX2-(sum(Xs)**2)/len(Xs))

b = y_av - m * x_av

print('y={:.2f}x+{:.1f}'.format(m, b))
