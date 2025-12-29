import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里生成两个整数 l, r，范围控制在 [0, 2^n - 1]
    upper = max(1, 2 ** n - 1)
    l = random.randint(0, upper)
    r = random.randint(0, upper)

    # 原始逻辑
    z = l ^ r
    c = 0
    if z == 0:
        print(0)
        return
    while z:
        c += 1
        z >>= 1
    x = '1' * c
    print(int(x, 2))

# 示例调用
if __name__ == "__main__":
    main(5)