n=int(input())
tmp = 0
num = 0

for i in range(n):
    tmp = int(input()) * (10**(n-i-1))
    num += tmp

print(num*2)