def main(n):
    # Generate deterministic input data: n integers
    # Example: l[i] = i + 1
    l = [i + 1 for i in range(n)]
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
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)