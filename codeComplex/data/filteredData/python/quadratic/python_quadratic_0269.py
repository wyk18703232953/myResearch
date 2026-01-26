n = 0
m = 0
x = []
y = []


def generate_data(n):
    global x, y, m
    n = max(1, n)
    # 定义 x 为长度 n 的序列
    x = [i * 2 for i in range(n)]
    # 定义 y 为长度 n 的序列，其中一半来自 x，一半不在 x 中
    y = []
    for i in range(n):
        if i % 2 == 0:
            y.append(x[i])

        else:
            y.append(i * 2 + 1)
    m = len(y)


def core_logic():
    global x, y, m
    l = []
    for i in range(m):
        if y[i] in x:
            l.append(x.index(y[i]))
    l.sort()
    output = []
    for i in l:
        output.append(str(x[i]))
    if output:
        # print(" ".join(output))
        pass


def main(n):
    generate_data(n)
    core_logic()


if __name__ == "__main__":
    main(10)