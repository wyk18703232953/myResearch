import random

def main(n):
    # 1. 生成测试数据
    # 设定：
    #   x = n                         列表长度
    #   y = n * 10 + 5                目标值
    #   z = n * 2 + 1                 初始值
    #   l 为长度为 x 的正整数列表
    x = n
    y = n * 10 + 5
    z = n * 2 + 1

    # 生成列表 l，元素为 1 到 20 之间的随机整数
    random.seed(0)  # 固定随机种子，方便复现
    l = [random.randint(1, 20) for _ in range(x)]

    # 2. 原始逻辑（去掉 input() 后的实现）
    l.sort()
    c = 0
    s = z
    while s < y and c < x:
        c += 1
        s = s + l[x - c] - 1
    if s < y:
        print(-1)
    else:
        print(c)

if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)