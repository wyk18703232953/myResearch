import math
import random

def main(n):
    # 生成规模为 n 的测试数据，这里生成 1~10 的随机整数
    t = [random.randint(1, 10) for _ in range(n)]

    p = sum(t)
    a = math.ceil(p / 2)

    u = 0
    for j in range(n):
        u += t[j]
        if u >= a:
            print(j + 1)
            break

if __name__ == "__main__":
    # 示例：调用 main(5) 进行测试
    main(5)