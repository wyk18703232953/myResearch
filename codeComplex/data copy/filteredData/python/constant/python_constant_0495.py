import sys

def main(n):
    # n 作为规模参数，这里用于生成 Q 和每个查询的 N, M, K
    # 下面给出一种简单的测试数据生成方式：
    #
    # Q = n
    # 对于第 i 个查询：
    #   N = i
    #   M = n - i + 1
    #   K = n
    #
    # 可根据需要修改生成规则。

    Q = n
    results = []

    for i in range(1, Q + 1):
        N = i
        M = n - i + 1
        K = n

        if max(N, M) > K:
            results.append(-1)
            continue

        r = K
        if N % 2 != K % 2:
            r -= 1
        if M % 2 != K % 2:
            r -= 1
        results.append(r)

    # 输出结果
    for ans in results:
        # print(ans)
        pass
if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用中可以改成任意正整数
    main(10)