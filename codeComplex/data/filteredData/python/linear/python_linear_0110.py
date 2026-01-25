def main(n):
    # 对原程序的输入结构分析：
    # 原代码：n=int(input());print(sum(i for i in range(1+n%2!=1,n+1,2)))
    # 仅有一个整数输入 n，因此这里的 n 就直接作为规模参数和算法输入本身使用。
    #
    # 为了实验可规模化，这里仍然将 main 的参数 n 直接视为原程序的 n。
    #
    # 原逻辑回放：
    #   start = 1 + (n % 2 != 1)  # 若 n 为奇数，(n%2!=1) 为 False(0) -> 起点 1
    #                             # 若 n 为偶数，(n%2!=1) 为 True(1)  -> 起点 2
    #   然后从 start 到 n 每次步长 2 累加
    # 即：当 n 为奇数时，求 1,3,5,...,n 的和；
    #     当 n 为偶数时，求 2,4,6,...,n 的和。
    start = 1 + (n % 2 != 1)
    return sum(i for i in range(start, n + 1, 2))


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行规模化实验
    print(main(10))