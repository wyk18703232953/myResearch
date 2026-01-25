def main(n):
    if n <= 0:
        print(0)
        return
    l = [(i + 1) * 2 for i in range(n)]
    l.sort()
    vis = [0] * n
    ans = 0
    for i in range(n):
        if vis[i] == 0:
            ans += 1
            x = l[i]
            for j in range(n):
                if l[j] % x == 0:
                    vis[j] = 1
    print(ans)


if __name__ == "__main__":
    main(10)