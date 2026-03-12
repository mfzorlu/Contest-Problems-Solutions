# -1 or /2 problem

n = int(input())

hs = 0
if n % 2 == 0:
    win = "Ayla"
else:
    win = "Boran"


while n > 0:
    if n % 2 ==0:
        if n % 4 != 0:
            n /= 2
            hs += 1
        else:
            n -= 1
            hs += 1

    else:
        n -= 1
        hs += 1


print(win, str(hs))

