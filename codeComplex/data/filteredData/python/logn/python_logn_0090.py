def solve_range(l, r):
    def solve(n):
        arr = []
        while n > 0:
            arr.append(n % 2)
            n //= 2
        return arr

    arrl = solve(l)
    arrr = solve(r)
    if len(arrr) > len(arrl):
        ans = (1 << len(arrr)) - 1
        return ans
    else:
        ind = -1
        # 注意：solve 返回的是低位在前的列表
        for i in range(len(arrr) - 1, -1, -1):
            if arrr[i] != arrl[i]:
                ind = i
                break
        if ind == -1:
            return 0
        else:
            ans = (1 << (ind + 1)) - 1
            return ans


def main(n: int):
    """
    n 为测试规模，用于生成一组 (l, r) 测试数据并执行原逻辑。
    这里约定：
      - 1 <= l <= r <= n
      - 若 n < 2，则直接输出 0（无法构造有效区间）
    """
    if n < 2:
        print(0)
        return

    # 简单构造一组区间：l = n//2, r = n
    l = n // 2
    r = n
    if l == 0:
        l = 1
    if l > r:
        l, r = r, l

    ans = solve_range(l, r)
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 100 作为规模运行
    main(100)