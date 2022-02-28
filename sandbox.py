import math
from decimal import Decimal

sums = 0
for i in range(0, 10001):
    temp = Decimal(math.comb(10000, i))
    sums = sums +  temp * Decimal(((0.9)**(10000-i)) * ((0.1)**(i)))

print(sums)
