def main(n):
    from math import gcd

    lst1 = {}
    lst2 = {}
    lst = set()

    # Interpret n as: we will generate two lists, each of size n.
    # First list: keys 0..n-1, values = i*i
    # Second list: keys 0..n-1, values = i*(i+1)
    for i in range(n):
        x = i
        y = i * i
        lst1[x] = y
        lst.add(x)

    for i in range(n):
        x = i
        y = i * (i + 1)
        lst2[x] = y
        lst.add(x)

    ans = 0
    for i in lst:
        try:
            x = lst1[i]
        except:
            x = 0
        try:
            y = lst2[i]
        except:
            y = 0
        ans += max(x, y)

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)