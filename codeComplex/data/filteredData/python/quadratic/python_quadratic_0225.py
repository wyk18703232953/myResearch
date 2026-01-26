import sys


def main(n):
    # 保证 n 至少为 3，否则根据原逻辑无法进入主循环
    if n < 3:
        # print(-1)
        pass
        return

    # 确定性生成测试数据
    # a 为严格递增序列，b 为与下标相关的确定性值
    a = [i * 2 + 1 for i in range(n)]
    b = [(i * 3 + 5) for i in range(n)]

    ans = float('inf')
    for i in range(1, n - 1):
        bef = aft = float('inf')
        for j in range(i):
            if a[j] < a[i]:
                bef = min(bef, b[j])
        for j in range(i, n):
            if a[i] < a[j]:
                aft = min(aft, b[j])
        ans = min(ans, b[i] + bef + aft)
    # print(-1 if ans > 10 ** 9 else ans)
    pass
if __name__ == "__main__":
    main(10)