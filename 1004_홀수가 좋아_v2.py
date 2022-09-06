from collections import Counter
input()
number_list = [i for i in map(int, input().split()) if i % 2 == 1]
number_counter = Counter(number_list)
max_number = number_counter.most_common(1)[0][1]
print(max([k for k, v in number_counter.items() if v == max_number]))