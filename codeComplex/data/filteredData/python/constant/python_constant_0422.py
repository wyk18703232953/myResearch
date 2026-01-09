def main(n):
    # 这里根据 n 生成测试数据，示例：让 k 在合理范围内变化
    # 你可以根据实际需要修改生成方式
    results = []
    for k in range(1, 2 * n + 1):
        if k > n + (n - 1):
            ans = 0

        else:
            if k <= n:
                ans = (k - 1) // 2

            else:
                x = n - (k - n)
                ans = (x + 1) // 2
        results.append((k, ans))
    return results


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改或删除
    out = main(10)
    for k, val in out:
        # print(f"k={k}, result={val}")
        pass