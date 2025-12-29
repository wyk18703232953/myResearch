import random

def main(n):
    # 参数设置：可以根据需要调整
    L = n * 10          # 下界
    R = n * 50          # 上界
    X = 10              # 最大最小差值下限
    max_c_value = 50    # 元素最大值
    min_c_value = 1     # 元素最小值

    # 生成测试数据：n 个随机整数
    c = [random.randint(min_c_value, max_c_value) for _ in range(n)]

    l, r, x = L, R, X

    ans = 0
    for mask in range(1, 1 << n):  # 从1开始，避免空集合
        v = []
        for j in range(n):
            if mask & (1 << j):
                v.append(c[j])
        if not v:
            continue
        s = sum(v)
        if l <= s <= r and (max(v) - min(v) >= x):
            ans += 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)