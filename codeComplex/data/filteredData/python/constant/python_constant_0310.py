import math
import random

def main(n: int):
    # 生成测试数据
    # 保证 s, p 在合理范围内且不为 0
    k = random.randint(1, max(1, n))
    s = random.randint(1, max(1, n))
    p = random.randint(1, max(1, n))

    # 原逻辑
    x = math.ceil(n / s)
    y = math.ceil(x * k / p)
    print(y)

if __name__ == "__main__":
    # 示例调用，规模可自行修改
    main(100)