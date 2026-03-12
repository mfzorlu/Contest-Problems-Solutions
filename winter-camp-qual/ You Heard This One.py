X, Y = list(map(int, input().split()))

n = Y-X+1


for i in range(1337):
    if n < 2**i:
        print(i)
        break