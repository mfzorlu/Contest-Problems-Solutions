t = int(input())

def calc(x:int, y:int) -> int:
    
    return x*y


for i in range(t):
    A, B, X, Y = list(map(int, input().split()))
    
    XD = A-X-1
    YD = B-Y-1
    
    rec1 = calc(X, B)
    rec2 = calc(Y, A)
    rec3 = calc(XD, B)
    rec4 = calc(YD, A)
    
    recs = [rec1, rec2, rec3, rec4]
    
    result = 0
    for j in range(4):
        if result < recs[j]:
            result = recs[j]
    
    print(result)
    