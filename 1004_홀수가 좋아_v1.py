def checker(number_list):
    counter = dict()
    number_list = sorted(number_list, reverse=True)
    def check_prime_number(number):
            if number % 2 == 1:
                return True
            return False
    i = 0
    while i < len(number_list):
        _ = number_list[i]
        i+=number_list.count(_)
        if check_prime_number(_):
            counter[_] = number_list.count(_)
    if not counter:
        return 0
    counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    counter_max = counter[0][1]
    return max([k for k, v in counter if v == counter_max])

input()
number_list = map(int, input().split())
print(checker(number_list))