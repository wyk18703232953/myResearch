def main(n):
    # 映射：给定规模 n，构造一个确定性的 (n, a, b)
    # 条件来自原代码逻辑：
    #   - 若 min(a, b) > 1 或 (n, a, b) in {(2,1,1), (3,1,1)} 则输出 "NO"
    #   - 为了保障对大部分 n 有非平凡结构，这里固定 a,b 为:
    #       * n == 2: (2,1,1) -> NO 分支
    #       * n == 3: (3,1,1) -> NO 分支
    #       * 其他:  a = 1, b = 1
    if n == 2:
        a, b = 1, 1
    elif n == 3:
        a, b = 1, 1

    else:
        a, b = 1, 1

    if min(a, b) > 1 or ((n, a, b) in ((2, 1, 1), (3, 1, 1))):
        # print("NO")
        pass
        return

    res = [[0] * n for _ in range(n)]
    for i in range(0, n - max(a, b)):
        res[i][i + 1] = 1
        res[i + 1][i] = 1
    if a == 1:
        res = [[e ^ 1 for e in l] for l in res]

    # print("YES")
    pass
    for i in range(n):
        res[i][i] = 0
        # print(*res[i], sep='')
        pass
if __name__ == "__main__":
    # 示例：按规模调用，可自行修改或在实验脚本中循环调用
    main(5)