from itertools import product

N = input()
M = int(input())
if M != 0:
    unworkButton = input().split()
    workButton = '0123456789'
    for i in unworkButton:
        workButton.replace(i,"")
    lis = product(workButton, repeat=len(N))

min = 500000
for i in lis:
    gap = abs(int("".join(i))-int(N))
    if gap < min:
        min = gap
print(min)