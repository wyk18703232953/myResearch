import sys
import math
def rec(i,n,l):
    # print(i,l)
    if i == n:
        return []

    else:
        x = l2[i]
        flag = 0
        o = []
        p = []
        mi = -1
        for j in l:
            if j < x:
                if j > mi:
                    if i == 0 and j == 0:
                        o.append(j)
                        p.append(j)
                        continue

                    mi = j

            if x == j:
                flag = 1

            o.append(j)
            p.append(j)

        if flag:
            o.remove(x)

        if mi == -1 and flag == 0:
            return []

        ans1 = []
        if flag:
            # print(i,o)
            ans1 = [x]+rec(i+1,n,o)

        if mi != -1:
            p.remove(mi)

        p.sort(reverse = True)
        ans2 = [mi]+p
        if len(ans1) == n-i:
            return ans1

        else:
            return ans2

for _ in range(1):
    a = int(input())
    b = int(input())
    e1 = str(a)
    e2 = str(b)
    l1 = []
    l2 = []
    for i in e1:
        l1.append(int(i))

    for i in e2:
        l2.append(int(i))

    if len(l1) < len(l2):
        l1.sort(reverse = True)
        o = []
        for i in l1:
            o.append(str(i))

        print("".join(o))

    else:
        n = len(l2)
        ans = rec(0,n,l1)
        w = []
        for i in ans:
            w.append(str(i))

        print("".join(w))