def main(n):
    k = max(1, n % 20 + 1)
    arr = [((i * 3 + 7) ^ (i // 2)) % (1 << k) for i in range(1, n + 1)]
    newarr = [0]
    for num in arr:
        newarr.append(newarr[-1] ^ num)
    dic = {}
    limit = (1 << k) - 1
    for num in newarr:
        x = (min(num, limit - num), max(num, limit - num))
        if x in dic:
            dic[x] += 1

        else:
            dic[x] = 1
    ans = 0
    for elem in dic:
        m = dic[elem]
        half = m // 2
        ans += half * (half - 1) / 2
        half = m - half
        ans += half * (half - 1) / 2
    ans = n * (n + 1) / 2 - ans
    # print(int(ans))
    pass
if __name__ == "__main__":
    main(10)