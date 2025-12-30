import random

def main(n):
    # ---------- 生成测试数据 ----------
    # 生成长度为 n 的数组 b，元素范围 [0, min(n-1, 2023)]
    max_val = min(n - 1, 2023) if n > 0 else 0
    if n <= 0:
        print(0)
        return
    b = [random.randint(0, max_val) for _ in range(n)]

    # ---------- 原 shrink 逻辑（已封装为函数） ----------
    def shrink_array(arr):
        shrinked_array = arr[:]
        while True:
            done = True
            for i in range(0, len(shrinked_array) - 1):
                if shrinked_array[i] == shrinked_array[i + 1]:
                    done = False
                    shrinked_array.pop(i + 1)
                    shrinked_array[i] = shrinked_array[i] + 1
                    break
            if done:
                break
        return len(shrinked_array)

    # 可选：调用 shrink_array 以展示其作用（如不需要可删除）
    _ = shrink_array(b)

    # ---------- 原主逻辑（去除 input） ----------
    # e = 2D 数组，大小 [2024][n+1]，初值 -1
    e = [[-1] * (n + 1) for _ in range(2024)]
    # d = 长度为 n 的列表，每个元素为列表
    d = [[] for _ in range(n)]

    # 填充 e 和 d
    for i, v in enumerate(b):
        if 0 <= v < 2024:  # 防御性判断
            e[v][i] = i
            d[i].append(i)

    for v in range(1, 2024):
        for i in range(n):
            j = e[v][i]
            h = e[v][j + 1] if j != -1 and j + 1 <= n else -1
            if j != -1 and h != -1:
                e[v + 1][i] = h
                d[i].append(h)

    a = [i for i in range(1, n + 1)]
    for s in range(n):
        for pos in d[s]:
            if s > 0:
                a[pos] = min(a[pos], a[s - 1] + 1)
            else:
                a[pos] = min(a[pos], 1)

    print(a[n - 1])


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)