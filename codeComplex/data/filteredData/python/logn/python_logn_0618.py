import math
import random

def main(n):
    # 生成测试数据：
    # 设定 numTimePut 为 1 到 n 之间的随机整数
    numTimePut = random.randint(1, n)
    # 再随机选择一个 numEat，使得 (numEat + numTimePut) 不超过 n
    max_numEat = max(0, n - numTimePut)
    numEat = random.randint(0, max_numEat)
    # 按照原注释关系构造 k：
    # (numEat + numTimePut) = n0
    # ((numTimePut*(numTimePut+1))//2) - numEat = k
    n0 = numEat + numTimePut
    k = (numTimePut * (numTimePut + 1)) // 2 - numEat

    # 现在用原公式中的 n = n0, k 进行计算
    n_val = n0
    k_val = k
    result = int(n_val - (math.sqrt(8 * (n_val + k_val) + 9) - 3) / 2)
    print(result)

if __name__ == "__main__":
    # 示例：以 n = 10 为规模运行
    main(10)