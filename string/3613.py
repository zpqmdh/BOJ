# Java vs C++
import sys
input = sys.stdin.readline

word = input().rstrip()
conv_word = ''
flag = False # Java
upper = False # 대문자
if '_' in word:
    flag = True # C++
def is_error(word):
    if 'A' <= word[0] <= 'Z':
        return True
    if '_' == word[-1] or word[0] == '_':
        return True
    if '_' in word and word != word.lower():
        return True
    if '__' in word:
        return True
    return False
if flag: # C++ -> Java
    for w in word:
        if w == '_':
            upper = True
        elif upper:
            conv_word += w.upper()
            upper = False
        else:
            conv_word += w
else: # Java -> C++
    for w in word:
        if 'A' <= w <= 'Z':
            conv_word += '_'
            conv_word += w.lower()
        else:
            conv_word += w

if is_error(word):
    print("Error!")
else:
    print(conv_word)