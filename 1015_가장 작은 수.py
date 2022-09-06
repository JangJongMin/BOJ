def factorize2(n): #https://upgrade-j.tistory.com/entry/python%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%86%8C%EC%9D%B8%EC%88%98-%EB%B6%84%ED%95%B4-%ED%95%98%EA%B8%B0
    factor = 2 #시작 소수 지정
    factors = []
    while (factor**2 <= n):  # 에라토스테네스를 떠올리며,, 즉 루트n까지 실행
        while (n % factor == 0):  # 소수로 나누어 떨어지면(= 즉 약수면)
            factors.append(factor)  # 리스트에 추가
            n = n // factor  # n을 몫으로 변경
        factor += 1
    if n > 1 : # 1보다 크고 factor**2(4)보다 작은 경우 n은 소수임으로 append -> 2,3 경우
        factors.append(n)
    return factors

def solutation(numbers):
    two = numbers.count(2)
    three = numbers.count(3)
    while two > 1 or two+three > 1:
        if two >= 3:
            two -= 3
            numbers.remove(2)
            numbers.remove(2)
            numbers.remove(2)
            numbers.append(8)
        elif three >= 2:
            three -= 2
            numbers.remove(3)
            numbers.remove(3)
            numbers.append(9)
        elif two >= 1 and three >= 1:
            two -= 1
            three -= 1
            numbers.remove(2)
            numbers.remove(3)
            numbers.append(6)
        elif two > 1:
            two -= 2
            numbers.remove(2)
            numbers.remove(2)
            numbers.append(4)
        else:
            print("ERROR")
            exit()
    return sorted(map(str, numbers))

number = int(input())
factorize_number = factorize2(number)
if len(factorize_number) < 1 or max(factorize_number) > 10:
    print(-1)
else:
    print("".join(solutation(factorize_number)))