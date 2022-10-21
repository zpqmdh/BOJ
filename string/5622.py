# 다이얼
string_number = input()
dial = {2: "ABC", 3: "DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}
ans = []
for i in range(len(string_number)):
	for j in range(2, 10):
		if string_number[i] in dial[j]:
			ans.append(j)
print(sum(ans) + len(ans))