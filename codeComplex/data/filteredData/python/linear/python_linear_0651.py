from collections import defaultdict
import random

def main(n):
    # 1. 生成测试数据
    # 生成数组元素范围 [-5, 5]，并保证 tar 存在于数组中
    if n <= 0:
        print(0)
        return

    a = [random.randint(-5, 5) for _ in range(n)]
    tar = random.choice(a)  # 确保 tar 在数组中

    # 2. 原始逻辑开始
    d = defaultdict(lambda: [])
    count = 0
    for i in range(n):
        d[a[i]].append(i)
        if a[i] == tar:
            count += 1

    presum = [1 if a[0] == tar else 0]
    for e in a[1:]:
        if e == tar:
            presum.append(presum[-1] + 1)
        else:
            presum.append(presum[-1])

    final = 0
    for k, v in d.items():
        if k == tar:
            continue

        t = 1
        tt = 1
        for i in range(1, len(v)):
            ind = v[i]
            preind = v[i - 1]

            t -= presum[ind] - presum[preind]
            t = max(t, 0)
            t += 1
            tt = max(tt, t)

        final = max(final, tt)

    print(final + count)


if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)