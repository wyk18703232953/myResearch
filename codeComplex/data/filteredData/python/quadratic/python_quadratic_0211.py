from functools import reduce
from operator import ior
import random

def main(n):
    # n 代表 nk 的规模，这里同时也用作 m 的规模（比特长度）
    nk = max(2, n)          # 至少 2 个，否则原逻辑直接 "NO"
    m = max(1, n)           # 至少 1 位二进制

    # 生成测试数据：nk 个随机 m 位二进制数
    # 为了可控，这里用随机数；如需可重复性，可设置随机种子
    a = []
    for _ in range(nk):
        # 生成 0 到 2^m - 1 的随机数
        val = random.getrandbits(m)
        a.append(val)

    if nk == 1:
        print("NO")
        return

    num = reduce(ior, a)
    for i in range(nk):
        k = a.copy()
        k.pop(i)
        n_val = reduce(ior, k)
        if n_val == num:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改或删除
    main(5)