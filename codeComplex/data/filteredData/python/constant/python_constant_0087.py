import math
import random

def main(n: int):
    # 根据 n 生成测试数据，这里使用 n 作为算法输入规模
    # 若希望进行多组测试，可自行在外部循环调用 main 不同的 n
    m = 0
    limit = min(100, n)
    for i in range(limit):
        for ii in range(limit):
            for iii in range(limit):
                i1 = n - i
                ii1 = n - ii
                iii1 = n - iii
                r1 = (i1 * ii1) // math.gcd(i1, ii1)
                r2 = (r1 * iii1) // math.gcd(iii1, r1)
                m = max(m, r2)
    print(m)

if __name__ == "__main__":
    # 示例：自动生成一个规模 n 进行测试
    # 这里随机生成 1~1000 内的 n 作为测试规模
    test_n = random.randint(1, 1000)
    main(test_n)