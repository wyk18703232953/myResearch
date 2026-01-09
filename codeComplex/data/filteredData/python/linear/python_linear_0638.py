from __future__ import division

def main(n):
    """
    生成规模为 n 的测试数据并运行原逻辑。
    测试数据规则示例：
      - 若 n == 1: a = [1]
      - 若 n == 2: a = [2, 2]
      - 若 n >= 3: 前一半为 >=2 的点，后一半为 1
    可按需修改生成规则。
    """
    # --------- 1. 生成测试数据 a ---------
    if n <= 0:
        return

    a = [0] * n
    if n == 1:
        a = [1]
    elif n == 2:
        a = [2, 2]

    else:
        half = n // 2
        for i in range(half):
            a[i] = 2  # 可以接 2 条边
        for i in range(half, n):
            a[i] = 1  # 叶子

    # --------- 2. 原逻辑开始（去除输入输出封装） ---------
    cap = [0] + a[:]  # 1-based capacity

    ones = []
    others = []

    for i in range(n):
        if a[i] == 1:
            ones.append(i + 1)

        else:
            others.append(i + 1)

    outputs = []

    def write(x):
        outputs.append(str(x))

    if len(others) == 0:
        if len(ones) == 1:
            write("YES 0")
            write("0")

        else:
            write("NO")
        # 打印结果
        # print("\n".join(outputs))
        pass
        return

    dia = len(others)
    graph = []

    # 把所有非 1 的点连成一条链
    for j in range(len(others) - 1):
        graph.append((others[j], others[j + 1]))
        cap[others[j]] -= 1
        cap[others[j + 1]] -= 1

    # 尝试在两端挂 1
    if len(ones) > 0:
        this = ones.pop()
        graph.append((this, others[0]))
        cap[others[0]] -= 1
        dia += 1

    if len(ones) > 0:
        this = ones.pop()
        graph.append((this, others[-1]))
        cap[others[-1]] -= 1
        dia += 1

    # 把剩下的 1 尽量挂到还有容量的非 1 点上
    done = False
    for j in range(len(others)):
        while cap[others[j]] > 0:
            if len(ones) > 0:
                this = ones.pop()
                graph.append((this, others[j]))
                cap[others[j]] -= 1

            else:
                done = True
                break
        if done:
            break

    if len(ones) > 0:
        write("NO")

    else:
        write("YES " + str(dia - 1))
        write(len(graph))
        for u, v in graph:
            write(f"{u} {v}")

    # --------- 3. 输出 ---------
    # print("\n".join(outputs))
    pass
if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(5)