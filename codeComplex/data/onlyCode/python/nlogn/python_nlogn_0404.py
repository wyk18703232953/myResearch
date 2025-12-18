from sys import stdin, stdout

get_string = lambda: stdin.readline().strip('\n')
get_intmap = lambda: map( int, get_string().split(' ') )
#get_intmap

def testcase():
    n = int(input())
    cnt = dict()
    for i in range(n):
        l,r = get_intmap()
        cnt[l] = cnt.get(l,0) + 1
        cnt[r+1] = cnt.get(r+1,0) - 1
    ans = [0] * (n + 1)
    sk = sorted(cnt.keys())
    #print(cnt)
    cnt_i = 0
    for ind, i in enumerate(sk[:-1]):
        cnt_i += cnt[i]
        ans[cnt_i] += sk[ind + 1] - i
    print(' '.join([str(i) for i in ans[1:]]))
        

    

testcase();quit()
for t in range(int(input())):
    testcase()
