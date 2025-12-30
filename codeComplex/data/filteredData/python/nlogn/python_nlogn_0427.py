from math import *
from collections import Counter
import random

def main(n):
    # 生成规模为 n 的测试数据：元素在 [-(10**9), 10**9] 范围内
    a = [random.randint(-10**9, 10**9) for _ in range(n)]
    
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
    print(ans)

if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)