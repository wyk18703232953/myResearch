import sys
import random

def solve_one(n, s):
    if 2 * s > n * (n + 1) or s < 2 * n - 1:
        return None  # impossible

    for i in range(n, -1, -1):
        if i == 0:
            branch = 1
            break
        tmp = 0
        tmpn = n
        j = 1
        while tmpn - i ** (j - 1) >= 0:
            tmp += j * (i ** (j - 1))
            tmpn -= i ** (j - 1)
            j += 1
        tmp += j * tmpn
        if tmp > s:
            branch = i + 1
            break

    tmp = 0
    tmpn = n
    j = 1
    i = branch
    dic = {}
    while tmpn - i ** (j - 1) >= 0:
        tmp += j * (i ** (j - 1))
        dic[j] = (i ** (j - 1))
        tmpn -= i ** (j - 1)
        j += 1
    tmp += j * tmpn
    dic[j] = tmpn
    maxi = j

    while tmp < s:
        for j in range(maxi, -1, -1):
            if j not in dic:
                continue
            while dic[j] > 1:
                if s - tmp + j <= maxi:
                    dic[j] -= 1
                    dic[s - tmp + j] = dic.get(s - tmp + j, 0) + 1
                    tmp = s
                else:
                    dic[j] -= 1
                    dic[maxi + 1] = dic.get(maxi + 1, 0) + 1
                    tmp += maxi + 1 - j
                    maxi += 1
                if tmp == s:
                    break
            if tmp == s:
                break

    b = []
    for key in dic:
        for _ in range(dic[key]):
            b.append(key)
    b.sort()

    children = [0] * n
    ans = [-1] * n
    curr = 0
    for i in range(1, n):
        while b[i] > b[curr] + 1:
            curr += 1
        ans[i] = curr
        children[curr] += 1
        if children[curr] == branch:
            curr += 1

    finans = []
    for i in range(1, n):
        finans.append(ans[i] + 1)
    return finans


def generate_s(n):
    # minimal sum of depths: 2*n - 1 (star)
    # maximal sum of depths: n*(n+1)//2 (path)
    min_s = 2 * n - 1
    max_s = n * (n + 1) // 2
    return random.randint(min_s, max_s)


def main(n):
    # generate a single test with size n
    if n <= 1:
        print("YES")
        return

    s = generate_s(n)
    res = solve_one(n, s)
    if res is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    # example: run with some default n, or adapt externally
    main(10)