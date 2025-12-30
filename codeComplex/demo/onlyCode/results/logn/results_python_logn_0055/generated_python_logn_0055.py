import math
import random

def Maxxor(l, r):
    if l == r:
        return 0
    else:
        reflog = math.floor(math.log2(r))
        ref = 2 ** reflog
        if l < ref:
            return (2 * ref) - 1
        else:
            return Maxxor(l - ref, r - ref)

def main(n):
    # 根据规模 n 生成测试数据：
    # 1. 生成一个上界 max_val，确保其位数与 n 相关
    # 2. 随机生成 l, r，满足 0 <= l <= r <= max_val
    if n <= 0:
        n = 1

    # 让 max_val 大约在 [2^(n-1), 2^n) 范围内
    max_val = (1 << n) - 1  # 2^n - 1

    l = random.randint(0, max_val)
    r = random.randint(l, max_val)

    ans = Maxxor(l, r)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数，可自行修改
    main(10)