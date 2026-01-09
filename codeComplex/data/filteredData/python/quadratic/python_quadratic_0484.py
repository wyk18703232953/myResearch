def main(n):
    # 解释输入结构：
    # 原程序使用：
    #   n
    #   left[0..n-1]
    #   right[0..n-1]
    #
    # 为了可规模化与确定性，这里用 n 控制数组长度：
    # 构造一种既有 0 又有非 0 的确定性模式，以保证算法有非平凡行为。
    # left[i] = i % 3
    # right[i] = (n - 1 - i) % 3

    left = [i % 3 for i in range(n)]
    right = [(n - 1 - i) % 3 for i in range(n)]
    res = [0] * n
    val = n

    if all(not left[i] and not right[i] for i in range(n)):
        # print("YES")
        pass
        # print(' '.join(['1'] * n))
        pass
        return

    while not all(not left[i] and not right[i] for i in range(n)):
        zeroSet = set()
        for i in range(n):
            if not left[i] and not right[i] and res[i] == 0:
                zeroSet.add(i)
                res[i] = val
        for v in zeroSet:
            for i in range(v + 1, n):
                if i not in zeroSet and res[i] == 0:
                    left[i] -= 1
            for i in range(v):
                if i not in zeroSet and res[i] == 0:
                    right[i] -= 1
        val -= 1
        if not zeroSet:
            # print("NO")
            pass
            return

    for i in range(n):
        if not res[i]:
            res[i] = str(val)

        else:
            res[i] = str(res[i])
    if any(i == '0' for i in res):
        # print("NO")
        pass
        return
    # print("YES")
    pass
    # print(' '.join(res))
    pass
if __name__ == "__main__":
    # 示例：使用 n=10 运行主函数
    main(10)