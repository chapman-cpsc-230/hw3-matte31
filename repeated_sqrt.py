from math import sqrt

for n in range (1,60):
    r = 2.0
    for i in range (n):
        r = sqrt(r)
    for i in range (n):
        r = r**2
    print '%d times sqrt and **2: %.16f' %(n,r)
#takes the number r and taking the square root of the number then squaring that
for n in range (1,60):
    r = 2.0
    for i in range (n):
        r = sqrt(r)
    for i in range (n):
        r = r**2
