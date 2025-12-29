import random

def main(n):
    # 生成测试数据：n 个随机整数，范围可根据需要调整
    vals = [random.randint(0, 100) for _ in range(n)]

    # 按原逻辑排序
    vals.sort()

    flag = 0

    for i in vals:
        if i > vals[0]:
            print(i)
            flag = 1
            break

    if flag == 0:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行修改
    main(10)