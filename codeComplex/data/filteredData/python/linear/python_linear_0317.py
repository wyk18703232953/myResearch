from random import randint

def main(n):
    # 1. 生成测试数据
    # 规模 n 为数组长度；为了有意义地测试，设 m 也与 n 有关
    # 这里设 m = max(1, n // 3)（可按需要修改生成规则）
    if n <= 0:
        return

    m = max(1, n // 3)

    # 生成 arr：元素范围可随意设定，这里设在 [0, 10^9]
    arr = [randint(0, 10**9) for _ in range(n)]

    # 2. 将原逻辑封装，无 input()
    s = sum(arr)
    idx = [[] for _ in range(m)]
    for i in range(n):
        idx[arr[i] % m].append(i)

    j = 0
    for i in range(m):
        while len(idx[i]) > n // m:
            while True:
                if j < i:
                    j += 1
                elif len(idx[j % m]) >= n // m:
                    j += 1
                else:
                    break
            last = idx[i].pop()
            arr[last] += (j - i) % m
            idx[j % m].append(last)

    print(sum(arr) - s)
    print(*arr)


if __name__ == "__main__":
    # 示例：调用 main，规模可自己调整
    main(10)