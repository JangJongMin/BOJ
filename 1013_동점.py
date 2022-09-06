from collections import Counter

input()
_ = Counter(map(int, input().split())).most_common()
print(max([number for number, count  in _ if count == _[0][1]]))
