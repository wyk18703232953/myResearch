import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里令 k 在 [1, 3*n] 区间内随机
    k = random.randint(1, 3 * n)

    q = 2 * n + 1
    p = k // n
    if k % n:
        print(p + 1)
    else:
        print(p)

if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(10)