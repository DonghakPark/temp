"""
분수 찾기 문제
Author : DongHak Park
Contact: donghark03@naver.com
"""

X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(a, '/', b, sep='') 