import math
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 原程序读取 n, k，其中 n 可以看作规模，这里保持 n 不变，随机生成 k
    k = random.randint(0, max(1, n * 10))

    # 原始公式：print(int((2*n+3-(8*n+8*k+9)**(1/2))//2))
    # 直接复用逻辑
    result = int((2 * n + 3 - math.sqrt(8 * n + 8 * k + 9)) // 2)
    print(result)


if __name__ == "__main__":
    # 示例调用：规模可自行调整
    main(10)