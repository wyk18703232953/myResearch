from math import *
from collections import *

def main(n):
    # 生成确定性的测试数据：长度为 n 的整数数组
    # 这里采用简单的算术构造，包含重复值和不同大小的数
    a = [(i * 3) % (2 * n + 1) for i in range(n)]

    d = Counter(a)
    ans = 0
    for i in range(n):
        for j in range(31):
            s = 2 ** j
            s = s - a[i]
            if d.get(s) is not None and ((d[s] == 1 and s != a[i]) or d[s] >= 2):
                break

        else:
            ans += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)