def main(n):
    # Interpret n as the number of elements
    if n <= 0:
        print(0)
        return

    # Deterministically construct parameters l, r, x based on n
    l = n
    r = 3 * n
    x = max(1, n // 5)

    # Deterministically construct the list num of length n
    num = [(i * 2 + 3) % (3 * n + 7) + 1 for i in range(n)]

    ans = 0
    for mask in range(2 ** n):
        st = bin(mask)[2:]
        st = '0' * (n - len(st)) + st
        if st.count('1') >= 2:
            pt = []
            for i in range(len(st)):
                if st[i] == '1':
                    pt.append(num[i])
            s = sum(pt)
            if l <= s <= r and max(pt) - min(pt) >= x:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main(10)