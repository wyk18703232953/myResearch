import random

def main(n: int):
    # 生成测试数据：
    # x 为长度 n 的随机整数序列
    # m 为查询次数，这里设为 n，y 从 x 中随机选择，保证部分或全部命中
    random.seed(0)  # 固定种子，方便复现
    x = [random.randint(0, 100) for _ in range(n)]
    m = n
    y = [random.choice(x) for _ in range(m)]

    # 原逻辑
    l = []
    for i in range(m):
        if y[i] in x:
            l.append(x.index(y[i]))
    l.sort()
    for i in l:
        print(x[i], end=" ")

if __name__ == "__main__":
    # 示例：规模为 10，可根据需要修改
    main(10)