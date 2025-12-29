import random

def sum_list(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s

def main(n):
    # 根据规模 n 生成测试数据：n 个 1~100 的随机整数
    cns = [random.randint(1, 100) for _ in range(n)]

    xs, nm, c = 0, 0, 0
    cns.append(0)
    while xs <= nm:
        m = max(cns)
        cns.remove(m)
        xs += m
        nm = sum_list(cns)
        c += 1
    print(c)

if __name__ == "__main__":
    # 示例：运行时可修改 n 测试不同规模
    main(10)