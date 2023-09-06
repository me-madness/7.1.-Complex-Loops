n = int(input())

for row in range(n):
    for col in range(n):
        num = col + row + 1 
        if num > n:
            num = 