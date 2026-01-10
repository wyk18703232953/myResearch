from collections import Counter

def main(n):
    # Deterministically generate array 'a' of length n
    # Values are within a moderate range to allow sums of powers of two
    a = [(i * 7) % 1000 for i in range(n)]

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
    main(10)