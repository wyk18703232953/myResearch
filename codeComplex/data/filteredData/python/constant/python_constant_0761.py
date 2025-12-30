import math
import random

def main(n: int):
    # 生成测试数据：
    # 原式中有 n、k，其中 n 为规模；这里令 k 与 n 同级随机
    k = random.randint(0, n * 10)

    ans = ((2 * n + 3) - int(math.sqrt(8 * n + 8 * k + 9))) // 2
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模自定
    main(100)