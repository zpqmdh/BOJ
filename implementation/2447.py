# 별 찍기 - 10
'''
참고) https://cotak.tistory.com/38
'''
def append_star(length):
    if length == 1:
        return ['*']
    stars = append_star(length//3)
    L = []
    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s + ' '*(length//3) + s)
    for s in stars:
        L.append(s*3)
    return L
    
N = int(input())
print('\n'.join(append_star(N)))