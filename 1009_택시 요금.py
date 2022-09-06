import math

a, b ,c ,d = map(int,input().split())

if a >= b:
    print(a)
else:
    print(a + c * math.ceil((b-a)/(c+d)))
