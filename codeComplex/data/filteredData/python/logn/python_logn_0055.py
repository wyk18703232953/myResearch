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
    # 在区间 [0, 2^n - 1] 中随机生成 l, r，并保证 l <= r
    if n <= 0:
        n = 1
    upper = (1 << n) - 1
    l = random.randint(0, upper)
    r = random.randint(0, upper)
    if l > r:
        l, r = r, l

    ans = Maxxor(l, r)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(5)