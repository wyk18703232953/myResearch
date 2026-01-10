def main(n):
    def solve(n, arr):
        arr = sorted(arr)
        a = arr[-2]
        return min(n - 2, a - 1)

    # 解释输入结构映射：
    # 原程序结构为：
    # T
    # n
    # arr (长度为 n)
    # 所以这里将 n 作为测试用例数量 T
    # 每个用例的规模也设为 n，数组长度为 n
    
    T = n
    total_result = 0

    for t in range(1, T + 1):
        cur_n = n
        # 构造确定性的数组，长度为 cur_n
        # arr[i] = (i % cur_n) + 1，保证元素为正整数
        arr = [(i % cur_n) + 1 for i in range(cur_n)]
        # 为了避免所有元素过小导致负值影响，可再平移一部分
        arr = [x + (t % 5) for x in arr]
        total_result += solve(cur_n, arr)

    print(total_result)


if __name__ == "__main__":
    main(10)