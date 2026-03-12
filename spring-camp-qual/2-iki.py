n = int(input())
nums = list(map(int, input().split()))

def abs_valude(a):
    if a<0:
        return a*(-1)
    return a


TOTAL = (sum(nums))

best = 10**16 + 7
for i in range(n):

    if abs_valude(TOTAL-nums[i])<best:
        best=abs_valude(TOTAL-nums[i])

print(best)
