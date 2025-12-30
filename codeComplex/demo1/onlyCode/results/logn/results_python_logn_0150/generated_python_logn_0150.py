# 转换后的程序：去除 input()，封装为 main(n, k)，并可根据 n 生成测试数据

def normal_sum(N):
    return (N ** 2 + N) // 2

def seg_sum(i, j):
    # 原函数名为 sum，避免覆盖内置函数，这里改名为 seg_sum
    return normal_sum(j) - 1 - (normal_sum(i - 1) - 1)

def bs_sum(start, end, k, n):
    # 二分搜索
    if start > end:
        # 按原逻辑不太会走到这里，这里给一个兜底返回
        return 0
    mid = (start + end) // 2

    remain = n - seg_sum(mid, k)
    if remain >= mid:
        return bs_sum(start, mid - 1, k, n)
    if remain < 0:
        return bs_sum(mid + 1, end, k, n)

    return k - mid + 2 if remain != 0 else k - mid + 1

def solve(n, k):
    # 原题逻辑封装为函数：给定 n, k 返回答案（不打印）
    if n == 1:
        return 0
    if n <= k:
        return 1
    # 判断是否可行
    if normal_sum(k) - 1 - (k - 2) < n:
        return -1

    n -= 1
    k -= 1
    return bs_sum(1, k, k, n)

def main(n, k=None):
    """
    n: 规模
    k: 参数，如果不提供则基于 n 自动生成一个测试用 k
    返回：对应的答案（不打印）
    """
    # 根据 n 生成测试数据：若 k 未给定，则构造一个合理的 k
    # k 至少为 1，且适当与 n 同量级，方便测试
    if k is None:
        # 保证 k >= 1
        # 这里取一个与 n 同数量级但不小于 1 的 k
        # 例如：k = min(n, 2 * int(n**0.5) + 1) 仅为测试数据构造示例
        from math import isqrt
        k = min(n, 2 * isqrt(max(n, 1)) + 1)

    return solve(n, k)

# 示例：如需直接运行测试，可取消下面注释
# if __name__ == "__main__":
#     print(main(10))        # 自动生成 k
#     print(main(10, 5))     # 指定 k