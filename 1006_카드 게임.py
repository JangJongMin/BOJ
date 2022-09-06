from collections import Counter

def straight_cheker(card):
    _ = [1,2,3,4,5,6,7,8,9,10,11,12,13]*2
    for i in range(13):
        if card == sorted(_[i:i+5]):
            return True
    return False

card = list(map(int, input().split()))[:5]

card.sort()
card_count = Counter(card)
              
if card_count.most_common(1)[0][1] == 4:
    print("poker")
elif len([i for index, i in enumerate(card_count.most_common(2)) if i[1] == 3 - index]) == 2:
    print("full")
elif straight_cheker(card):
    print("straight")
elif card_count.most_common(1)[0][1] == 3:
    print("triple")
elif len([i for index, i in enumerate(card_count.most_common(2)) if i[1] == 2]) == 2:
    print("two")
elif card_count.most_common(1)[0][1] == 2:
    print("one")
else:
    print("high")