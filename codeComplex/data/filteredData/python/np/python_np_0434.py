import random

def check(mid: int, a, n, m, ans_holder) -> bool:
    dic = {}
    for i in range(n):
        bit = 0
        for j in range(m):
            if a[i][j] >= mid:
                bit += 1
            bit <<= 1
        dic[bit >> 1] = i
    full = (1 << m) - 1
    for x, idx in dic.items():
        for y, idy in dic.items():
            if x | y == full:
                ans_holder[0] = (idx + 1, idy + 1)
                return True
    return False


def main(n: int):
    # 根据 n 生成测试数据
    # 约定列数 m，保持与原算法一致（m 不宜过大）
    m = min(8, max(1, n if n < 8 else 8))  # 简单选择：最多 8 列
    # 生成数值在 [0, 1e9] 的随机矩阵
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    ans_holder = [(-1, -1)]

    le = 0
    ri = 10**9
    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid, a, n, m, ans_holder):
            le = mid + 1
        else:
            ri = mid - 1

    # 输出与原程序相同的内容：两个下标
    print(ans_holder[0][0], ans_holder[0][1])


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)