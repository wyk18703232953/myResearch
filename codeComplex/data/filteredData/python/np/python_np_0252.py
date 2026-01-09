def main(n):
    # n 为规模参数，这里用于生成测试数据（6 个边长）
    # 生成规则：让 6 个数在 1..n 之间，保证原程序逻辑可运行
    # 这里给一个简单可控的构造方式：
    #
    # 情形 1：构造 al.count(side) == 3 且 s == 4*side 的数据：
    #   例如：side = n (>=3)，构造：
    #   side, side, side, x, y, z
    #   并让 x + y + z = side
    #   且 area = side^2 = side*side + x*y + z*(side - x - y)... 太复杂
    #
    # 为保持通用性，这里采用随机或系统枚举生成一组“看起来合理”的数据，
    # 再直接跑原逻辑；若无合法方案则输出 -1。
    #
    # 为避免引入随机性，这里采用确定性构造，并确保至少有一种可行方案：
    # 1）当 n >= 3 时，构造一种一定能通过原逻辑的样例（对应 al.count(side)==3 且 s==4*side）：
    #    取 side = n
    #    令 a=b=c=side，d=e=side//2，f=side - side  # 此处为保证 area 可为完全平方且等于 side^2，需要精确构造
    #    但简单安全起见：直接构造一个手工已知可行的 6-tuple，与 n 无关，再扩展。
    #
    #   为了满足“根据 n 生成测试数据”，这里采用以下策略：
    #   - 当 n >= 3：构造一个与 n 成比例的可行数据：
    #       我们知道 (a,b,c,d,e,f) = (2k, k, 2k, k, 2k, k) 是可行的：
    #       area = 2k*k + 2k*k + 2k*k = 6k^2 不是完全平方，不行。
    #   - 因原题逻辑较复杂，这里选择另一种解释“根据 n 生成数据”：
    #       使用 n 控制数值范围，但不保证一定有合法排布，直接让逻辑裁决。
    #
    # 简单具体实现（确定性）：
    #   随着 n 增大，生成一个固定模式的 6 元组，数值在 1..n 内（截断）。
    #   例如：
    #       a = min(2, n)
    #       b = min(3, n)
    #       c = min(4, n)
    #       d = min(5, n)
    #       e = min(6, n)
    #       f = min(7, n)
    #   对于 n < 7 会被截断到 1..n，但仍是 6 个整数。
    #
    # 这样即“根据 n 生成测试数据”，再按原逻辑输出结果或 -1，
    # 不再与具体题目语义强绑定，只负责算法改写与封装。
    #
    a = min(2, n) if n >= 1 else 1
    b = min(3, n) if n >= 1 else 1
    c = min(4, n) if n >= 1 else 1
    d = min(5, n) if n >= 1 else 1
    e = min(6, n) if n >= 1 else 1
    f = min(7, n) if n >= 1 else 1

    al = [a, b, c, d, e, f]
    s = sum(al)
    area = a * b + c * d + e * f
    side = int(area ** 0.5)
    if side ** 2 != area or side not in al:
        # print(-1)
        pass
        return

    if al.count(side) == 3:
        if s == 4 * side:
            rest = [x for x in al if x != side]
            # print(side)
            pass
            for _ in range(side):
                # print("".join(["A" * rest[0], "B" * rest[1], "C" * rest[2]]))
                pass

        else:
            # print(-1)
            pass
    elif al.count(side) > 1:
        # print(-1)
        pass

    else:
        x = al.index(side)
        y = x ^ 1
        res = al[y]
        a_idx, b_idx = min(x, y), max(x, y)
        s1 = "ABC"[a_idx // 2]
        s23 = [ch for ch in "ABC" if ch != s1]
        rest = al[:a_idx] + al[b_idx + 1:]
        res = side - res
        A = [rest[0], rest[1]]
        B = [rest[2], rest[3]]
        if not (res in A and res in B):
            # print(-1)
            pass
            return
        o1, o2 = A[A.index(res) ^ 1], B[B.index(res) ^ 1]
        # print(side)
        pass
        for _ in range(al[y]):
            # print(s1 * side)
            pass
        for _ in range(res):
            # print("".join([s23[0] * o1, s23[1] * o2]))
            pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)