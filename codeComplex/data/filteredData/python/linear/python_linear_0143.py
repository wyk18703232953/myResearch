import random

def main(n):
    # 1. 生成测试数据：n 个非负整数，范围可按需调整
    m = [random.randint(0, n) for _ in range(n)]

    # 以下为原逻辑的无 input() 封装实现
    j = 0
    mark = [1]
    for i in range(1, len(m)):
        tmp = max(mark[i - 1], m[i] + 1)
        mark.append(tmp)

    j += mark[len(m) - 1] - m[len(m) - 1] - 1
    for i in range(len(m) - 2, -1, -1):
        if mark[i] < mark[i + 1] - 1:
            mark[i] = mark[i + 1] - 1
        j += mark[i] - m[i] - 1

    print(j)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)