from collections import Counter

def main(n):
    a = [(i * 3 + 7) % (2 ** 10) for i in range(n)]
    d = Counter(a)
    ans = 0
    for i in range(n):
        for j in range(31):
            s = 1 << j
            s = s - a[i]
            if d.get(s) is not None and ((d[s] == 1 and s != a[i]) or d[s] >= 2):
                break
        else:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main(1000)