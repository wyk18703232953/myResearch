def main(n):
    # n 表示测试用例数量 t
    t = n
    outputs = []

    for case_id in range(1, t + 1):
        # 为每个测试用例构造确定性的数组 a
        # 让数组长度随 case_id 变化，整体规模随 n 线性增长
        length = case_id * 4  # 每个用例长度递增
        # 构造一些重复元素，保证有多种情况：全相同、存在4个相同、只有2个相同等
        a = []
        base = case_id  # 与 case_id 相关，确定性
        for i in range(length):
            # 简单周期模式 + 偏移，保证确定性且包含重复
            val = (base + i // 2) % (2 * case_id + 3)
            a.append(val)

        # 原算法逻辑
        if len(set(a)) == 1:
            x = a[0]
            outputs.append(f"{x} {x} {x} {x}")
        else:
            a.sort()
            g1 = False
            d = {}
            mx = 10001
            for v in a:
                if v not in d:
                    d[v] = 1
                else:
                    d[v] += 1
                if d[v] == 4:
                    g1 = True
                    if v < mx:
                        mx = v
            if g1:
                outputs.append(f"{mx} {mx} {mx} {mx}")
            else:
                res = []
                for k in d.keys():
                    if d[k] >= 2:
                        res.append(k)
                m = len(res)
                if m < 2:
                    # 极端情况兜底（虽然构造里基本不会发生）
                    # 任意输出四个元素
                    x = a[0]
                    outputs.append(f"{x} {x} {x} {x}")
                else:
                    minj = 0
                    for j in range(m - 1):
                        if res[j]*res[j+1]*(res[minj]**2 + res[minj+1]**2) > res[minj]*res[minj+1]*(res[j]**2+res[j+1]**2):
                            minj = j
                    x1, x2 = res[minj], res[minj+1]
                    outputs.append(f"{x1} {x1} {x2} {x2}")

    # 统一输出，减少 I/O 噪音对时间测量的影响
    print("\n".join(outputs))


if __name__ == "__main__":
    main(10)