# 셀프 넘버
def d(n):
    for i in str(n):
        n += int(i)
    try:
        self_number.remove(n)
    except:
        pass
    return n

self_number = list(range(1, 10001))
for i in range(1, len(self_number)+1):
    res = d(i)
    
for number in self_number:
    print(number)

