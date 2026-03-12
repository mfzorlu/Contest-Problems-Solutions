n = int(input())
kgs = list(map(int, input().split()))

k=kgs[0]
b=kgs[0]

for i in range(n):
    if k > kgs[i]:
        k=kgs[i]
    if b < kgs[i]:
        b=kgs[i]

print(int(b-k))
