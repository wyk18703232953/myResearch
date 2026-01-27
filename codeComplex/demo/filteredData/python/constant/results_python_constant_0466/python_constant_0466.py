def main(n):
    # 解释输入结构与规模映射：
    # 原程序输入：
    # n (未使用)
    # (ax, ay)
    # (bx, by)
    # (cx, cy)
    #
    # 为进行时间复杂度实验，这里将 n 映射为要生成的测试用例数量。
    # 对于每个测试用例，构造一组三个点 (ax, ay), (bx, by), (cx, cy)。
    # 坐标构造采用确定性算术方式，与 i、n 相关，确保没有随机性且可规模化。
    #
    # 为保持与原程序逻辑一致，对每个测试用例执行同样的判断。

    results = []
    for i in range(1, n + 1):
        # 确定性生成三点坐标
        ax = i
        ay = n - i
        bx = -i
        by = i // 2
        cx = i * 2
        cy = (n + i) // 2

        if (bx < ax < cx) or (bx > ax > cx) or (by < ay < cy) or (by > ay > cy):
            results.append("NO")

        else:
            results.append("YES")

    # 为了避免输出过大，只输出最后一个结果，保证程序行为确定且可运行
    if results:
        # print(results[-1])
        pass

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    main(10)