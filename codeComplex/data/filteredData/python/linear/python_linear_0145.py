import random

def main(n: int):
    # 1. 生成测试数据 Ab，长度为 n 的非负整数序列
    # 可按需要修改生成规则
    Ab = [random.randint(0, 10) for _ in range(n)]

    Un = []
    Al = [0]
    r = 0

    # 对应原代码：读入并处理 Ab
    for i in range(n):
        # 原来这里有 Ab[i] = int(Ab[i])，现在 Ab 已是整数，可省略
        Al.append(max(Ab[i] + 1, Al[i]))

    # 从 n 到 0 进行后推修正
    for i in range(n, -1, -1):
        if Al[i - 1] < Al[i] - 1:
            Al[i - 1] = Al[i] - 1

    # 计算 Un 和结果 r
    for i in range(n):
        Un.append(Al[i + 1] - Ab[i] - 1)
        r += Un[-1]

    print(r)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)