from __future__ import division
import random

def main(n):
    # 生成测试数据：
    # n: 数组长度
    # m: 差值阈值，设为数组值范围的一部分
    # a: 长度为 n 的严格递增数组（可满足原逻辑中 a[i] - a[j] 相关条件）
    if n < 2:
        print(-1)
        return

    # 随机生成递增数组 a
    # 基数范围 [0, 10*n]，步长至少为 1 保证严格递增
    cur_val = random.randint(0, 5)
    a = []
    for _ in range(n):
        step = random.randint(1, 10)  # 保证递增
        cur_val += step
        a.append(cur_val)

    # 设置 m，取数组值范围的 1/3 作为阈值
    m = (a[-1] - a[0]) // 3 if n > 1 else 1
    if m <= 0:
        m = 1

    # 按原程序逻辑，注意原来有 a = rints()[::-1]
    # 这里同样做反转
    a = a[::-1]

    cur, ans = 2, -1

    for i in range(n - 2):
        cur = max(cur, i + 2)
        for j in range(cur, n):
            if a[i] - a[j] > m:
                break
            cur += 1
            v = (a[i] - a[j - 1]) / (a[i] - a[j])
            ans = max(ans, v)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)