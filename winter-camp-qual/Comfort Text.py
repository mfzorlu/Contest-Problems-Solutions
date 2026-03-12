N = int(input())

a_list  = list(map(int, input().split()))

SC = 0

for i in range(N-2):
    tmp = a_list[i] + a_list[i+1] + a_list[i+2]
    
    if tmp < 0:
        a_list[i+2] += tmp*(-1)
        SC += tmp*(-1)

print(SC)




"""
N = int(input())

a_list  = list(map(int, input().split()))

worst_case = 3 * 10**9 + 1

for i in range(N-2):
    tmp = a_list[i] + a_list[i+1] + a_list[i+2]
    
    if tmp < worst_case:
        worst_case = tmp
    

SC = worst_case*(-1)

if SC < 0:
    print(0)
else:
    print(SC)
"""