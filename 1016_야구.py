score = []
input()
numbers = input().split()
for i in numbers:
    if i == 0:
        continue
    if i == '5':
        score.append(1)
        continue
    if i >= '1':
        score.append(1)
    if i >= '2':
        score.append(0)
    if i >= '3':
        score.append(0)
    if i >= '4':
        score.append(0)
print(score[:-3].count(1))