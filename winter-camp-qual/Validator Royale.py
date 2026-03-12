"""
(!) Read this first:

I tried really hard, but the solution is missing.
So don't submit this version.

"""

# megaberke
#MB = "megaberke"


n = int(input())

cards = []
for i in range(n):
    cards.append(input()) 


"""if cards.count(MB):
    print("VALID")
    exit()"""   # HOCAM, AMAN HOCAM 


all_chars = []
for i in range(n):
    if not cards[i] in all_chars:
        all_chars.append(cards[i])
    #print(len(all_chars))
    if len(all_chars) > 8:
        print("INVALID")
        exit()


f = 0 # 8 kart + ayna mı kontrolu :O


if n < 5:
    
    ayna = 1
    chars = []
        
    for j in range(n):
        if not cards[j] in chars:
            chars.append(cards[j])
        else:
            f=1
            if ayna == 0:
                print("INVALID")
                exit()
            ayna = 0
            #print(chars.count(cards[j]))
            if chars.count(cards[j]) >= 2:
                print("INVALID")
                exit()
            else:
                chars.append(cards[j])


else:
    for i in range(n-4):
        
        ayna = 1
        chars = []
        tmp_list = cards[i:i+5]
        
        for j in range(5):
            if not tmp_list[j] in chars:
                chars.append(tmp_list[j])
            else:
                f=1
                if ayna == 0:
                    print("INVALID")
                    exit()
                ayna = 0
                #print(chars.count(tmp_list[j]))
                if chars.count(tmp_list[j]) >= 2:
                    print("INVALID")
                    exit()
                else:
                    chars.append(tmp_list[j])


if len(all_chars) == 8 and f == 1:
    print("INVALID")
    exit()


print("VALID")
