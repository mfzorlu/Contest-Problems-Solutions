import math
a, b, c = list(map(int, input().split()))

delta = b*b - 4*a*c

def solve(a, b, c, delta):

    if delta < 0:
        return "No roots"

    x1 = int((-1*b + math.sqrt(delta)) / (2*a))
    x2 = int((-1*b - math.sqrt(delta)) / (2*a))

    if delta == 0:
        return f"One root: {x1}"
    
    if x1 < x2:
        return f"Two roots: {x1} {x2}"
    
    return f"Two roots: {x2} {x1}"

print(solve(a, b, c, delta))
