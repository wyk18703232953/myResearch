import random

def main(n):
    # 生成测试数据：长度为 n 的整数序列，元素范围可自行调整
    l1 = [random.randint(-5, 5) for _ in range(n)]

    # 原逻辑
    if len(set(l1)) == 1 and l1[0] > 0:
        print(1)
    else:
        l2 = list(set(l1))
        x = l1.count(0)
        if x == 0:
            print(len(l2))
        else:
            print(len(l2) - 1)

if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(10)