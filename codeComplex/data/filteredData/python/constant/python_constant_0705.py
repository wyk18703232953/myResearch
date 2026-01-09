from operator import itemgetter

def main(n: int):
    # 生成测试数据：v 在 [0, n] 区间内取中间值
    v = max(0, min(n, n // 2))

    if v >= n - 1:
        ans = n - 1

    else:
        ans = v + ((2 + (2 + n - v - 2)) * (n - v - 1)) // 2

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需要修改
    main(10)