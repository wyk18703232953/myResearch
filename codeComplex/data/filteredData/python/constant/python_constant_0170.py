import sys, collections, math, itertools, random, bisect
INF = sys.maxsize
mod = 1000000007

def main(n):
    # 根据规模 n 生成测试数据 (l, r)
    # 这里选择生成一个较简单的区间 [l, r]，满足 r - l 与 n 相关
    # 你可以根据需求修改生成策略
    l = 1
    r = l + max(0, n - 1)  # 保证 r >= l，区间长度约为 n

    if r - l < 2:
        print(-1)
    elif l % 2 == 0:
        print(l, l + 1, l + 2)
    elif r - l > 2:
        print(l + 1, l + 2, l + 3)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)