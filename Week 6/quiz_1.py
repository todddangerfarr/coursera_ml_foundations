#Quiz 1 Question 3

#z1 = x1 AND x2
#z2 = ! x1 and ! x2
from itertools import product

x1 = [0, 1]
x2 = [0, 1]

z1a = [-0.5, -1, 1]
z2a = [1.5, -1, 1]

z1b = [-1.5, 1, 1]
z2b = [0.5, -1, -1]

y2 = [-0.5, 1, 1]

print '{}   {}   {}'.format('x1', 'x2', 'z1')

for tup in product(x1, x2):
	z1 = (z1a[0] + z1a[1] * tup[0] + z1a[2] * tup[1])
	thresholded = 0 if z1 < 0 else 1 
	print '{}    {}    {}    {}    {}'.format(tup[0], tup[1], z1, thresholded, tup[0] and tup[1])
	
print''

z1s = []
for tup in product(x1, x2):
	z1 = (z1b[0] + z1b[1] * tup[0] + z1b[2] * tup[1])
	thresholded = 0 if z1 < 0 else 1 
	z1s.append(thresholded)
	print '{}    {}    {}    {}    {}'.format(tup[0], tup[1], z1, thresholded, tup[0] and tup[1])
	
print''

z2s = []
for tup in product(x1, x2):
	z2 = (z2b[0] + z2b[1] * tup[0] + z2b[2] * tup[1])
	thresholded = 0 if z2 < 0 else 1 
	z2s.append(thresholded)
	print '{}    {}    {}    {}    {}'.format(tup[0], tup[1], z2, thresholded, 1 if (not tup[0] and  not tup[1]) else 0) 

print''	

for index in range(0,4):
	y = y2[0] + z1s[index] * y2[1] + z2s[index] * y2[2]
	thresholded = 0 if y < 0 else 1 
	print '{}    {}    {}     {}'.format(z1s[index], z2s[index], y, thresholded)