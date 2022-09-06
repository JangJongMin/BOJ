import random

n = random.randint(1, 10)
m = random.randint(1, 30)
print(n, m)
for i in range(n):
    print(' '.join(random.choices(['0','1'], k=m)))