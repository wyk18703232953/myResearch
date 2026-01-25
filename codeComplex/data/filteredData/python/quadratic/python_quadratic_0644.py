n=10**5

def main(n):
    l = [i + 1 for i in range(n)]
    l.sort()
    v = [False for _ in range(n)]
    ans = 0
    i = 0
    while i < n:
        if not v[i]:
            ans += 1
            for j in range(i + 1, n):
                if l[j] % l[i] == 0:
                    v[j] = True
        i += 1
    print(ans)


if __name__ == "__main__":
    main(n)