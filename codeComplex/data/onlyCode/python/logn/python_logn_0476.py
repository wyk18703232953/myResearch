from sys import stdout
# https://codeforces.com/problemset/problem/1088/D

#a, b = 10009090, 209090909

def get_ans(c, d, curaM, curbM):
    a_ = a ^ c ^ curaM
    b_ = b ^ d ^ curbM
    
    if a_ > b_:
        return 1
    
    if a_ < b_:
        return -1
    
    return 0

def get_ans_(c, d, curaM, curbM):
    a_ = c ^ curaM
    b_ = d ^ curbM
    
    print('? {} {}'.format(a_, b_))
    stdout.flush()
    
    return int(input())
    
curaM  = 0
curbM  = 0
curC   = get_ans_(0,0,0,0)

for i in range(29, -1, -1):
    ans1 = get_ans_(1<<i, 0, curaM, curbM)
    ans2 = get_ans_(0, 1<<i, curaM, curbM)
    
    if ans1 * ans2 >= 0:
        if curC == 1:
            curaM |= 1 << i
        elif curC == -1:
            curbM |= 1 << i
            
        curC = ans1    
    else:
        if ans1 < 0:
            curaM |= 1 << i
            curbM |= 1 << i
            
print('! {} {}'.format(curaM, curbM))            