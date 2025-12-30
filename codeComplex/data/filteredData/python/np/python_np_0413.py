from collections import defaultdict
import random


def main(n):
    # 生成测试数据
    # 固定列数 m，也可根据需要修改为与 n 相关
    m = 5
    # 生成 n 行 m 列的随机整数矩阵，数值范围与原程序二分上界相匹配
    arr = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    def check(num):
        bitmask = set()
        for i in range(n):
            b = 0
            for j in range(m):
                if arr[i][j] >= num:
                    b ^= 1 << j
            bitmask.add(b)
        target = (1 << m) - 1
        for i in bitmask:
            for j in bitmask:
                if (i | j) == target:
                    return True
        return False

    # 二分查找最大满足条件的阈值 ans
    start = 0
    end = 10 ** 9
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if check(mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    # 根据 ans 找到具体的两行编号
    bitmask = defaultdict(list)
    for i in range(n):
        b = 0
        for j in range(m):
            if arr[i][j] >= ans:
                b += 1 << j
        bitmask[b].append(i + 1)
    target = (1 << m) - 1
    for i in bitmask:
        for j in bitmask:
            if (i | j) == target:
                print(bitmask[i][0], bitmask[j][0])
                return


if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(6)