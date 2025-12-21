def fibonacci(n):
    flist = []
    a = 0
    b = 1
    flist.append(a)
    flist.append(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        if b < n:
            flist.append(b)
        else:
            flist.append(b)
            break
    return flist

def twopinter(li, i, x):
    z = 0
    while i <= len(li) - 1 and z <= len(li) - 1:
        if li[i] + li[len(li) - 1 - z] == x:
            return li[i] + li[len(li) - 1 - z]
        elif li[i] + li[len(li) - 1 - z] < x:
            i += 1
        elif li[i] + li[len(li) - 1 - z] > x:
            z += 1
        else:
            return 0
    return 0

def threepointer(li, n):
    st = 0
    while st <= len(li) - 1:
        x = n - li[st]
        if li[st] + twopinter(li, st, x) == n:
            return True
        elif li[st] + twopinter(li, st, x) < n:
            st += 1
        else:
            return False
    return False

def main(n):
    li = fibonacci(n)
    if not threepointer(li, n):
        return "I'm too stupid to solve this problem", 0, 0, n
    return "", 0, 0, n

if __name__ == "__main__":
    res = main(10)
    if isinstance(res, tuple):
        for item in res:
            print(item)
    else:
        print(res)