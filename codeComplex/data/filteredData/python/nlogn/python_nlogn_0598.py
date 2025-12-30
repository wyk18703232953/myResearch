from collections import Counter as C
import random

def main(n: int):
    # 生成测试数据：
    # n 对应原程序中的 n（数组长度）
    # 这里令 m = n，数组元素在 [1, m] 均匀随机
    m = n
    l = [random.randint(1, m) for _ in range(n)]

    c = sorted(C(l).items())

    res = 0
    j = 0
    for hi, ni in c:
        h = min(hi - j, ni) + j
        res += (hi - 1) * ni
        if h > j:
            j = h

    max_l = max(l)
    if j < max_l:
        res -= max_l - j

    print(res)


if __name__ == "__main__":
    # 示例：可根据需要修改规模
    main(10)