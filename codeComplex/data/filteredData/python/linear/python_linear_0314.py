from collections import deque
import random

def main(n: int):
    # 生成测试数据
    # 选择 m，确保 m <= n 且 m >= 1
    m = max(1, n // 3)
    # 生成 n 个非负整数，数值范围适当放大，以产生多样的模分布
    arr = [random.randint(0, 10 * m) for _ in range(n)]

    mods = [0 for _ in range(m)]
    placement = [[] for _ in range(m)]

    for i in range(n):
        r = arr[i] % m
        mods[r] += 1
        placement[r].append(i)

    cnt = 0
    queue = deque()
    target = n // m

    for i in range(2 * m):
        mod = i % m
        if mods[mod] > target:
            # 将多余的元素放入队列等待调整
            excess = mods[mod] - target
            for c in range(excess):
                queue.append([mod, placement[mod][c]])
            mods[mod] = target
        elif mods[mod] < target:
            while queue and mods[mod] < target:
                prev_mod, idx = queue.popleft()
                delta = (mod - prev_mod) % m
                mods[mod] += 1
                cnt += delta
                arr[idx] += delta

    print(cnt)
    print(' '.join(str(x) for x in arr))


if __name__ == "__main__":
    # 示例：运行规模为 n=10
    main(10)