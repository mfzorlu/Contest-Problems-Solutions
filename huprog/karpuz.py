n = int(input())
if n <= 1:
    print("Ooops!")
    exit()

karpuzlar = list(map(int, input().split()))

k=karpuzlar[0]
b=karpuzlar[0]

for i in range(n):
    
    if k > karpuzlar[i]:
        k=karpuzlar[i]
    if b < karpuzlar[i]:
        b=karpuzlar[i]


print(k, b)
