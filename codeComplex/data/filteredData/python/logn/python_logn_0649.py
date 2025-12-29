# https://codeforces.com/problemset/problem/1195/B
# 转换说明：
# 1. 去掉了 input()，逻辑封装在 main(n) 中。
# 2. 根据 n 自动生成一个合法的 k（这里选取中间范围的值）。
# 3. 返回结果，而不是打印；如需打印可在外层调用 print(main(n))。

def main(n):
    # 生成测试数据：k 在 [0, n*(n+1)//2] 范围内
    # 该题中实际可行的 k 范围更窄，但这么取保证合法
    total_pairs = n * (n + 1) // 2
    # 选择一个适中的 k，避免极端情况都在边界
    k = total_pairs // 2

    def check(mid):
        added = n - mid
        total = added * (added + 1) // 2
        return total - mid >= k

    low = 0
    high = n - 1
    while low < high:
        mid = (low + high + 1) // 2
        if check(mid):
            low = mid
        else:
            high = mid - 1

    return low

# 示例：如需运行测试
if __name__ == "__main__":
    n = 10
    result = main(n)
    print(result)