a = int(input())
b = int(input())

while b != 0:
    old_b = b
    b = a % b
    a = old_b
print('GCB = %d' % a)    
