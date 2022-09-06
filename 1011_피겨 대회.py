from collections import Counter

n = int(input())

people = Counter()
for i in range(n):
    _ = list(map(int, input().split()))
    people[sum(_) - max(_) - min(_)] += 1
    
print(max(people), people[max(people)])
