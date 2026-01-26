#import random

def max_xor_naive(l, r):
    max_xor = 0
    xor = 0

    for a in range(l, r+1):
        for b in range(a+1, r+1):
            xor = a^b
            if xor>max_xor:
                max_xor = xor

    return max_xor

def max_xor_efficient(l, r):
    s1 = bin(l)[2:]
    s2 = bin(r)[2:]
    l1 = len(s1)
    l2 = len(s2)
    if l1<l2:
        return pow(2, l2) - 1
    x = 0
    for i in range(0, l1):
        if s1[i]!=s2[i]:
            return pow(2, l1-i) - 1

    return 0

#while True:
l, r = map(int, input().split())
#l = int(input())
#r = int(input())
#    l = random.randint(1, 1000)
#    r = random.randint(l, 1000)
    #print(max_xor_naive(l, r))
    #print(max_xor_efficient(l, r))
    #print("Input: ", l, r)
    #ans1 = max_xor_naive(l, r)
ans2 = max_xor_efficient(l, r)
print(ans2)
    #print("Ans Naive:", ans1)
    #print("Ans Efficient: ", ans2)

'''
    if ans1==ans2:
        print("Verified OK")
    else:
        print("Wrong Answer")
        break
'''
