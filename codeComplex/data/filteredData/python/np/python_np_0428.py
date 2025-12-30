import random

def main(n):
    """
    n: 数组个数（规模）。每个数组长度 m 也在内部生成。
    逻辑：与原程序相同——二分一个阈值 check，使得存在两行的“>= check”掩码按位或为全 1。
    """
    # 1. 生成测试数据
    #   这里示例：m = n（你可按需修改为其他规则）
    #   元素值在 [0, 10^9] 内随机生成
    m = max(1, n)  # 确保 m >= 1
    arrays = [
        [random.randint(0, 10**9) for _ in range(m)]
        for _ in range(n)
    ]

    full = (1 << m) - 1
    L = -1
    R = 10**9 + 1

    ans0 = 0
    ans1 = 0

    while L + 1 < R:
        check = (L + R) >> 1

        masks = {}
        for i, arr in enumerate(arrays):
            curr = 0
            for val in arr:
                curr <<= 1
                if val >= check:
                    curr |= 1
            masks[curr] = i

        isValid = False
        for k1 in masks:
            for k2 in masks:
                if k1 | k2 == full:
                    ans0 = masks[k1]
                    ans1 = masks[k2]
                    isValid = True
                    break
            if isValid:
                break

        if isValid:
            L = check
        else:
            R = check

    # 模拟原程序的输出（1-based 索引）
    print(ans0 + 1, ans1 + 1)


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)