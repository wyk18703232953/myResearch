import random

def main(n: int):
    # 生成测试数据：长度固定为 4，与原程序一致
    # n 作为生成数据的规模上界
    lis = [random.randint(0, n) for _ in range(4)]

    # 原逻辑
    if lis[2] <= lis[0] and lis[2] <= lis[1]:
        if (lis[0] + lis[1] - lis[2]) < lis[3]:
            print(lis[3] - (lis[0] + lis[1] - lis[2]))
        elif sum(lis) == 0:
            print(-1)
        elif lis[0] == 0 and lis[1] == 0 and lis[2] == 0:
            print(lis[3])
        else:
            print(-1)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)