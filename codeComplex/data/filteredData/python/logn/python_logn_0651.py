import math

def main(n):
    # 生成测试数据：k 的范围大致在 [0, n*(n+1)//4]
    # 这里给一个简单的构造方式：让 k 依赖于 n，保证随规模变化
    k = n * (n + 1) // 4

    def possible(a, b):
        koyta = a * (a + 1) // 2
        return koyta >= b + k

    ans = 0
    lo = 0
    hi = n

    while hi >= lo:
        mid = (hi + lo) // 2
        if possible(n - mid, mid):
            lo = mid + 1
            ans = mid
        else:
            hi = mid - 1

    print(ans)


if __name__ == "__main__":
    # 示例运行：可根据需要调整 n
    main(10)