def main(n):
    V = []
    for i in range(n):
        x = i * 2 + 1
        w = (i % 3) + 1
        V.append((x - w, x + w))
    if n == 0:
        # print(0)
        pass
        return
    V.sort(key=lambda x: x[1])
    ans = 1
    now = V[0]
    for i in range(1, n):
        if V[i][0] >= now[1]:
            now = V[i]
            ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)