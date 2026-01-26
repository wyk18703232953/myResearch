def main(n):
    arr = [i % 5 for i in range(n)]
    ans = 0
    s = 0
    mp = {}
    for i in range(n):
        x = arr[i]
        ans += (x * i) - s
        ans -= mp.get(x - 1, 0)
        ans += mp.get(x + 1, 0)
        mp[x] = mp.get(x, 0) + 1
        s += x
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)