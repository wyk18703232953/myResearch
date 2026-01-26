# https://codeforces.com/problemset/problem/701/C
# two pointers method


def main():
    n = int(input())
    s = input()

    u_set = set()
    for i in s:
        u_set.add(i)
    u_cnt = len(u_set)

    d = {}
    j = 0
    ans = 10**9
    for i in range(n):
        while len(d.keys()) < u_cnt and j < n:
            d[s[j]] = d.get(s[j], 0) + 1
            j += 1

        if len(d.keys()) == u_cnt:
            if j - i < ans:
                ans = j - i
        elif j == n:
            break

        d[s[i]] -= 1
        if d[s[i]] == 0:
            del d[s[i]]

    print(ans)


if __name__ == '__main__':
    main()
