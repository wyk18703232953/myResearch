import random

def main(n):
    # 生成测试数据：构造一个满足原逻辑的序列示例
    # 目标：恰好有一个严格峰值，其他位置不是峰也不是谷且不相等
    # 简单构造：严格递增到中点，再严格递减（典型“山脉”）
    if n < 3:
        # 原逻辑对 n<3 没意义，这里直接打印 NO
        print("NO")
        return

    peak_pos = n // 2  # 峰位置索引
    a = list(range(1, peak_pos + 2))  # 从 1 递增到峰值
    # 后半部分构造严格递减
    dec_part = list(range(a[-1] - 1, a[-1] - (n - peak_pos - 1) - 1, -1))
    a.extend(dec_part)

    # 原逻辑
    c = 0
    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            c += 1
        if a[i] == a[i - 1] or a[i] == a[i + 1]:
            print('NO')
            return
        if a[i] <= a[i - 1] and a[i] <= a[i + 1]:
            print('NO')
            return

    if c > 1:
        print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)