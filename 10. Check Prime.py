import math
n = int(input())
prime = True

for i in range(2, int(math.sqrt(n) + 1)):
    if n % i ==0:
        prime = False
        break
if prime:
    print('Prime')
else:
    print('Not prime')        