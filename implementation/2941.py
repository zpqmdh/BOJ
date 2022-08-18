# 크로아티아 알파벳
arr = input()
c_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in c_alphabet:
    arr = arr.replace(i, '!')
print(len(arr))
