a = input().split(" ")
# Oo, it aaa is not bb.

def pal(s):
        
        #if s[j] == '.' or s[j] == ',' or s[j] == ':' or s[j] == '!' or s[j] == '-' or s[j] == ';' or s[j] == '?' or s[j] == '\'' or s[j] == '(' or s[j] == ')' or s[j] == '"':

    for i in range(len(s)/2):
        if s[i] != s[-i-1]:
            return False
    return True

MAX=0
result=0
for e in range(len(a)):
    if pal(a[e]) and len(a[e]) > MAX:
        MAX=len(a[e])
        result=e

