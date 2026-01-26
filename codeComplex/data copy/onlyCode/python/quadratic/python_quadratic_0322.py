import sys

def pprint(s):
    sys.stdout.write(str(s) + "\n")

def solve(n, d, k):
    for i in range(1, d+1):
        pprint(str(i)  + ' ' + str(i+1))
        if i + 1 == n:
            exit()

    q = d+2
    for i in range(2, d+1):
        for j in range(k-2):
            pprint(str(i)  + ' ' + str(q))
            if q == n:
                exit()
            q += 1
            def rec(depth, current, head):
                if depth == 0:
                    return current

                for i in range(k-1):
                    pprint(str(head)  + ' ' + str(current))
                    if current == n:
                        exit()
                    current += 1
                        
                    current = rec(depth-1, current, current-1)

                return current

            if i <= (d+2)/2:
                depth = i-2
            else:
                depth = d-i

            q = rec(depth, q, q-1)


    




n, d, k = map(int, input().split())

q = k-1
maxi = 0
if k == 2:
    maxi = d+1
else:
    if d % 2:
        maxi = (q * (1-q**(d//2)) // (1-q) + 1) * 2
    else:
        maxi = (q * (1-q**(d//2-1)) // (1-q) + 1) * 3 + 1

if d == 2:
    maxi = k + 1

if n > maxi or n <= d:
    print("NO")
else:
    print("YES")
    solve(n, d, k)