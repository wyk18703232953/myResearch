import math
import random

def maxor(bawah, atas):
    if bawah == atas:
        return 0
    xor_val = bawah ^ atas
    pangkat2 = math.log(xor_val, 2)
    return 2 ** int(math.floor(pangkat2) + 1) - 1

def main(n):
    # 根据规模 n 生成 n 对 (bawah, atas) 测试数据并逐个输出结果
    random.seed(0)
    results = []
    for _ in range(n):
        bawah = random.randint(0, 10**9)
        atas = random.randint(0, 10**9)
        if bawah > atas:
            bawah, atas = atas, bawah
        results.append(maxor(bawah, atas))
    for res in results:
        print(res)

if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)