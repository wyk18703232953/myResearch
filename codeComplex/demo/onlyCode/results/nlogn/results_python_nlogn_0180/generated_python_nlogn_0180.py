def main(n):
    V = []
    for i in range(n):
        x = i * 2
        w = 1
        V.append((x - w, x + w))
    if n == 0:
        return 0
    V.sort(key=lambda x: x[1])
    ans = 1
    now = V[0]
    for i in range(1, n):
        if V[i][0] >= now[1]:
            now = V[i]
            ans += 1
    return ans

if __name__ == "__main__":
    print(main(10))