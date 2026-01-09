def main(n):
    # 原程序逻辑：
    # 读入一个整数 n，按其值进行处理并输出
    # 为了可规模化，将构造一个长度为 n 的整数序列，对每个元素执行同样的逻辑
    # 构造方式：第 i 个数为 i*(-1)**i，使正负交替，规模与 n 线性相关
    results = []
    for i in range(n):
        x = i * (-1) ** i  # 可重复、确定性生成的“输入整数”

        # 以下是对单个整数 x 执行原始算法的逻辑
        if x >= 0:
            results.append(x)

        else:
            a = str(x)
            a = a[1::]
            if len(a) > 2:
                a_tmp = a[::-1][1::][::-1]
                num1 = int(a_tmp)

                a2 = str(x)
                a2 = a2[1::]
                b = a2[::-1]
                p1 = b[0]
                p2 = b[2::]
                p = p1 + p2
                p = p[::-1]
                num2 = int(p)

                small = min(num1, num2)
                results.append(-1 * small)
            elif len(a) == 2:
                m = a[0]
                n_char = a[1]
                small = min(int(m), int(n_char))
                results.append(-1 * small)

            else:
                # 对于长度为 1 的情况，原程序没有显式处理逻辑
                # 视为直接输出 x（与 "if x>=0" 对称处理）
                results.append(x)

    # 为了避免输出过大，仅在需要时可以打印最后一个结果
    if results:
        # print(results[-1])
        pass

    else:
        # print(0)
        pass
if __name__ == "__main__":
    # 示例调用，规模可自行调整
    main(10)