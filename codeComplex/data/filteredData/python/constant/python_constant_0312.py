import random

def main(n):
    # 生成规模为 n 的测试数据，这里生成 [0, 100] 范围内的随机整数
    a = [random.randint(0, 100) for _ in range(n)]

    mx = -1

    for i in range(14):
        if i >= n:
            break
        b = a.copy()
        if a[i]:
            b[i], d, ans = 0, i + 1, 0
            r = (a[i] + d) // 14
            l = (a[i] + d) % 14

            if d + a[i] < 14:
                # a[d:d + a[i]] 可能越界，需与 n 取 min
                right = min(d + a[i], n)
                ans = sum([j + 1 for j in a[d:right] if not (j + 1) % 2])
            else:
                for j in range(min(14, n)):
                    b[j] += r
                if d > l:
                    for j in range(l, min(d, n)):
                        b[j] -= 1
                else:
                    end = min(d + abs(d - l), n)
                    for j in range(d, end):
                        b[j] += 1
                ans = sum([p for p in b[:min(14, n)] if not p % 2])
            mx = max(mx, ans)

    print(mx)


if __name__ == '__main__':
    # 示例：运行 main，设置 n 的规模
    main(14)