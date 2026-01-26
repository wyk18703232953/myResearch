from sys import stdin, stdout

get_string = lambda: stdin.readline().strip('\n')
get_intmap = lambda: map( int, get_string().split(' ') )
#get_intmap

def testcase():
    n, M = get_intmap()
    a = [0] + list(get_intmap()) + [M]
    ontime = [0] * (n + 1)
    tmp = 0
    for ind in range(n, -1, -1):
        if ind %2 == 0: #light will be on from now
            tmp += a[ind + 1] - a[ind]#total ontime from ind
        ontime[ind] = tmp
    mx = ontime[0]
    #insert at ai + 1 or ai+1 - 1
    for ind in range(n + 1):#iterate over segments
        l,r = a[ind], a[ind+1]
        if r - l <= 1: continue
        for x in (l+1, r-1):
            newtime = ontime[0] - ontime[ind]
            if ind % 2 == 0:
                newtime += x - l
            else:
                newtime += r - x
            newtime += (M - r) - ontime[ind]
            mx = max(mx, newtime)
    print(mx)
        

    

testcase();quit()
for t in range(int(input())):
    testcase()
