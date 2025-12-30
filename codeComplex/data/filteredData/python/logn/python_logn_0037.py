import math
import random

def maxor(bawah, atas):
    if bawah == atas:
        return 0
    xor = bawah ^ atas
    pangkat2 = math.log(xor, 2)
    return 2 ** int(math.floor(pangkat2) + 1) - 1

def main(n: int):
    """
    n 为规模参数，用来控制测试数据的范围。
    示例：生成 [L, R]，其中 0 <= L <= R <= 2^n - 1
    """
    if n <= 0:
        # 退化情况，直接用一个固定区间测试
        bawah, atas = 0, 0
    else:
        max_val = (1 << n) - 1  # 2^n - 1
        bawah = random.randint(0, max_val)
        atas = random.randint(bawah, max_val)

    print(maxor(bawah, atas))

if __name__ == "__main__":
    # 示例：使用 n=10 作为规模，可根据需要修改
    main(10)