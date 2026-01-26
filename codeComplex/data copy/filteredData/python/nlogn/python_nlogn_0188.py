def main(n):
    a = [(i * 2) % (n // 2 + 1 if n // 2 + 1 > 0 else 1) for i in range(n)]
    ans = 0
    total_sum = 0
    mp = {}
    for i in range(n):
        x = a[i]
        ans += (x * i) - total_sum
        ans -= mp.get(x - 1, 0)
        ans -= -mp.get(x + 1, 0)
        mp[x] = mp.get(x, 0) + 1
        total_sum += x
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)