import sys
import math
import collections
import bisect
import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组，元素为 1~10^6 之间的随机整数
    # 可根据需要调整生成策略
    arr = [random.randint(1, 10**6) for _ in range(n)]

    counter = collections.Counter(arr)
    ans = set()
    for i in counter:
        for j in range(1, 32):
            no = 2 ** j
            diff = no - i
            if diff < 0:
                continue
            if diff == i:
                if counter[i] > 1:
                    ans.add(i)
                    break
            else:
                if diff not in counter:
                    continue
                else:
                    ans.add(i)
                    break

    val = 0
    ans = list(ans)
    for i in ans:
        val += counter[i]
    print(n - val)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)