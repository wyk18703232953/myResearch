def c(a, b, l, ans, pro):
    if l != 0:
        n = a[:]
        mx = None
        pro1 = pro
        prosh = set()
        for i in range(l):
            pro = pro1
            if a[i] == prosh:
                continue
            elif (a[i] <= b[0] and pro):
                n.pop(i)
                prosh = a[i]
                if pro == True:
                    if a[i] < b[0]:
                        pro = False
                m = c(n, b[1:], l-1, ans+str(a[i]), pro)
                n = a[:]
                if m != None:
                    if mx == None:
                        mx = int(m)
                    elif mx < int(m):
                        mx = int(m)
            elif not(pro):
                a.sort(reverse = True)
                a = list(map(str, a))
                return ans +''.join(a)
            else:
                break
        return mx            
    else:
        return ans
a = input()
b = input()
l = len(a)
if len(a) != len(b):
    a = list(a)
    a.sort()
    print(''.join(a[::-1]))
else:    
    a = list(map(int, a))
    b = list(map(int, b))
    a.sort()
    n = a[:]
    mx = 0
    prosh = -1
    for i in range(l):
        if a[i] == prosh:
            continue
        elif a[i] != 0 and a[i] <= b[0]:
            n.pop(i)
            prosh = a[i]
            pro = False
            if a[i] == b[0]:
                pro = True
            m = c(n, b[1:], l-1, str(a[i]), pro)
            n = a[:]
            if m != None:
                if mx < int(m):
                    mx = int(m)
        elif a[i] > b[0]:
            break
    print(mx)
    