def main(n):
    import random

    # 生成测试数据
    # 随机设置 m，保证至少为 1
    m = random.randint(1, min(10, n + 1))  # m 不宜过大，否则 2^m 太大，按需调整
    # 随机生成 a，元素范围与原程序二分上界一致 [0, 1e9]
    a = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    ans = [0, 0]  # 用列表替代全局可变变量，便于在闭包中修改

    def check(mid: int) -> bool:
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
                    ans[0], ans[1] = idx + 1, idy + 1
                    return True
        return False

    le = 0
    ri = 10**9
    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid):
            le = mid + 1
        else:
            ri = mid - 1

    # 按原程序风格输出答案
    print(ans[0], ans[1])


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)