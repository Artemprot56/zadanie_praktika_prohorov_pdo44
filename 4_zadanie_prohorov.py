#прохоров пдо44 4 задание

a = int(input("введите число для форматирвоания его в римские числа: "))
b = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

class Solution:
    def aToInt(self, S: str) -> int:
        ans = 0
        for i in range(len(S)-1,-1,-1):
            num = a[S[i]]
            if 4 * num < ans: ans -= num
            else: ans += num
        return ans
print(a)