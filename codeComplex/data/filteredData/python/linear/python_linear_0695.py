from collections import defaultdict as dd
import math

def main(n):
    # 将 n 映射为 (n, v) 的输入规模
    # 保证 v < n-1，大致使 v 与 n 同阶，便于做时间复杂度实验
    if n < 3:
        n_val = 3

    else:
        n_val = n
    v_val = (n_val - 1) // 2  # 0 <= v < n-1

    n_input, v_input = n_val, v_val

    n, v = n_input, v_input
    dist = n - 1

    if v >= dist:
        # print(dist)
        pass

    else:
        off = dist - v
        prices = [i + 2 for i in range(off)]
        # print(v + sum(prices))
        pass
if __name__ == "__main__":
    main(10)