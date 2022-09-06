from collections import deque

def rotation(x, y):
    x.rotate(y)
    return x

items = deque(input())
print(max([int(''.join(rotation(items,1))) for i in range(1, len(items)+1)]))