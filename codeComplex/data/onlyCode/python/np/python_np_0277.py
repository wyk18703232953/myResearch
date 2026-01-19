import math

p2 =[1] * 64

for i in range(1, 64):
    p2[i] = p2[i-1] * 2
    
def find_level(x):
    x0 = 1
    
    for i in range(max_level+1):
        if (x-x0) % (x0*2) == 0:
            return i
        x0 *=2
    
def move_U(number):
    cur_lv    =  find_level(number)
    
    if cur_lv == max_level:
        return number
    
    x0      =   p2[cur_lv]
    seg     =   x0 * 2 
    index   =  (number - x0) // seg
    
    return (x0*2) + (index // 2) * (seg * 2) 
    
def move_L(number):
    cur_lv    =  find_level(number)
    
    if cur_lv == 0:
        return number
    
    x0      =   p2[cur_lv]
    seg     =   x0 * 2 
    index   =  (number - x0) // seg
    
    return (x0 // 2) + (index * 2) * (seg // 2)

def move_R(number):
    cur_lv    =  find_level(number)
    
    if cur_lv == 0:
        return number
    
    x0      =   p2[cur_lv]
    seg     =   x0 * 2 
    index   =  (number - x0) // seg
    
    return (x0 // 2) + (index * 2 + 1) * (seg // 2)

def move(s,num):
    if s == 'U':
        return move_U(num)
    
    if s == 'L':
        return move_L(num)
    
    return move_R(num)
    
def process(S, num):
    for s in S:
        num = move(s, num)
    return num

n, q = map(int, input().split())
max_level = int(math.log2(n+1)) - 1
ans  = ''

for _ in range(q):
    num  = int(input())
    S    = input()
    ans += str(process(S, num)) + '\n'
    
print(ans)    

#15 2
#4
#UURL
#8
#LRLLLLLLLL