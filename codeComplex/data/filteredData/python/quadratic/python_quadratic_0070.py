def main(n):
    # n: length of array a and also number of queries q, both determined by n
    a = [i % 10 for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                cnt += 1
    even = cnt % 2 == 0

    q = n
    ans = []
    for t in range(q):
        l = t % n
        r = n - 1
        length = r - l + 1
        pairs = length * (length - 1) // 2
        if pairs % 2 == 1:
            even = not even
        if even:
            ans.append('even')
        else:
            ans.append('odd')
    print('\n'.join(ans))


if __name__ == "__main__":
    main(5)