def get_max(n):
    ans = 0
    while n:
        ans = 4 * ans + 1
        n = n - 1
        if ans > 10**19:
            break
    return ans

def solve_one(n, k):
    if n == 1:
        if k == 1:
            return "YES 0"
        else:
            return "NO"
    elif n == 2:
        if k <= 2:
            return "YES 1"
        elif k != 3 and k <= 5:
            return "YES 0"
        else:
            return "NO"
    else:
        siz = n - 1
        l = 1
        cnt = 3
        while siz:
            if l <= k < l + cnt:
                return "YES {}".format(siz)
            l = l + cnt
            cnt = 2 * cnt + 1
            siz = siz - 1
        else:
            if k <= get_max(n):
                return "YES 0"
            else:
                return "NO"

def main(n):
    t = n
    for i in range(1, t + 1):
        ni = i + 1
        ki = (i * i) % (10 * n + 10) + 1
        res = solve_one(ni, ki)
        print(res)

if __name__ == "__main__":
    main(5)