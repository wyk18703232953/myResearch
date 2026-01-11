def my_cmp(x):
    if x[0] == 0:
        return float('inf')
    return x[1] / x[0]

def dis(a, b):
    return a * a + b * b

def main(n):
    v = []
    for i in range(n):
        x = (i * 2 + 1) % (n + 3)
        y = (i * 3 + 2) % (n + 5)
        v.append((x, y, i))
    v.sort(key=my_cmp)
    x, y = 0, 0
    ans = [0] * n
    for i in range(n):
        if dis(x + v[i][0], y + v[i][1]) < dis(x - v[i][0], y - v[i][1]):
            ans[v[i][2]] = 1

        else:
            ans[v[i][2]] = -1
        x += v[i][0] * ans[v[i][2]]
        y += v[i][1] * ans[v[i][2]]
    for x in ans:
        # print(x, end=' ')
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)