a, b = input().split()
if hex(ord(a))[3] == hex(ord(b))[3]:
    print(0)
else:
    print(a if hex(ord(a))[3] > hex(ord(b))[3] else b)