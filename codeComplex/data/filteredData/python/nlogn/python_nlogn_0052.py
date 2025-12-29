import random

def main(n: int):
    # 1. 生成测试数据：长度为 n 的整数数组，元素范围可自行调整
    #   这里设为 1~10 之间的随机整数
    lista = [random.randint(1, 10) for _ in range(n)]

    # 原始逻辑开始
    pap = lista[:]
    pap.sort()
    if pap[-1] == 1:
        pap[-1] = 2
    else:
        pap = [1] + pap[:-1]

    # 输出结果
    for i in range(n):
        print(pap[i], end=" ")

# 示例调用
if __name__ == "__main__":
    main(5)