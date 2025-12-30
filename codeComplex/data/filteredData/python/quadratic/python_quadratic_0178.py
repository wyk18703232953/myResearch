import random

def main(n):
    # 生成测试数据：数组 a 的长度为 n，元素在 [0, 255] 内
    # 同时为每个用到的 a[i] 随机生成一个 k（1 到 256）
    a = [random.randint(0, 255) for _ in range(n)]
    k = random.randint(1, 256)

    c = [-1] * 256
    ans = [0] * n

    for i in range(n):
        if c[a[i]] == -1:
            for j in range(a[i], max(-1, a[i] - k), -1):
                if c[j] != -1:
                    if (c[j] + k) > a[i]:
                        c[a[i]] = c[j]
                    else:
                        c[a[i]] = j + 1
                    break
            if c[a[i]] == -1:
                c[a[i]] = max(0, a[i] - k + 1)
            for xx in range(c[a[i]], a[i]):
                c[xx] = c[a[i]]
        ans[i] = str(c[a[i]])

    print('n =', n)
    print('k =', k)
    print('a =', ' '.join(map(str, a)))
    print('result =', ' '.join(ans))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)