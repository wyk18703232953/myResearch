import random

def main(n: int):
    # 生成测试数据：
    # a,b 为基准点，范围 [-n, n]
    a = random.randint(-n, n)
    b = random.randint(-n, n)

    # 为了有一定概率输出 YES 和 NO，混合构造和随机构造
    def gen_point():
        return random.randint(-n, n), random.randint(-n, n)

    # 随机生成两个点 (b1,b2), (c1,c2)
    b1, b2 = gen_point()
    c1, c2 = gen_point()

    # 将原始逻辑中的平移操作应用到生成的数据
    b1 -= a
    b2 -= b
    c1 -= a
    c2 -= b

    # 原始判定逻辑
    if b1 == 0 or b2 == 0 or c1 == 0 or c2 == 0:
        print('NO')
    else:
        if b1 * c1 < 0 or b2 * c2 <= 0:
            print('NO')
        else:
            print('YES')


if __name__ == "__main__":
    # 示例调用：可按需修改 n
    main(10)