from collections import Counter
map_index = 2

def kernel_map(row, before_row):
    global map_index
    i = len(row)-1
    _ = map_index
    while i >= 0:
        if row[i] == 1:
            _ = row[i+1]
            if before_row[i] != 0:
                _ = before_row[i]
                temp = i
                while temp < len(row)-1:
                    if row[temp+1] != 0:
                        row[temp+1] = _
                    else:
                        break
                    temp+=1
                row[i] = _
            elif row[i+1] == 0:
                map_index+=1
                _ = map_index
            row[i] = _
        i-=1
    return row

#print(kernel_map([1, 0, 1, 1, 0, 0]))

n, m = map(int, input().split()[:2])
map_ = list()
map_index = 2
temp = [0 for i in range(m+2)]

#debug
map_debug = list()

for i in range(n):
    #열 체크 연속된 마을을 체크한다.
    _ = list(map(int, input().split()[:m]))
    temp=(kernel_map([0]+_+[0], temp))
    map_+= temp
    #debug
    map_debug.append(temp)

for i in map_debug:
    print('\t'.join(map(str, i)))

print([counting for number, counting in Counter(map_).most_common(2) if number != 0][0])