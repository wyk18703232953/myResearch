m = 10**18

def run():
    n, k = [int(x) for x in input().split()]
    currn, currs = 1, n
    rem = 0

    while True:
        if k == 0:
            print(f'YES {currs}')
            return
        if k < currn or currs == 0:
            print('NO')
            return
        currs -= 1
        k -= currn
        if currs >= 40:
            rem = m
        else:
            rem = min(m, rem + cc[currs]*((currn-1)*2+1))
        currn = (currn - 1) * 2 + 3

        if k <= rem:
            print(f'YES {currs}')
            return


cc = [0, 1]
for i in range(2, 50):
    cc.append(min(m, 1 + 4*cc[-1]))
for i in range(int(input())): run()
