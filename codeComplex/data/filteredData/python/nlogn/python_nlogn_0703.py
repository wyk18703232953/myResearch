from collections import defaultdict
import random

def find(A):
    A = sorted(A)
    N = len(A)
    dic = defaultdict(int)
    for i in range(N):
        dic[A[i]] += 1

    count = set()
    for x in A:
        if dic[x] > 2:
            return "cslnb"
        if dic[x] == 2:
            count.add(x)
            y = x - 1
            if y in dic:
                return "cslnb"

    if len(count) > 1:
        return "cslnb"

    if 0 in count:
        return "cslnb"

    temp = 0
    for i in range(N):
        temp += A[i] - i
    if temp % 2 == 1:
        return "sjfnb"
    return "cslnb"


def main(n):
    # 生成规模为 n 的测试数据：非负整数数组
    # 示例策略：从区间 [0, 2n] 中随机生成 n 个数
    A = [random.randint(0, 2 * n) for _ in range(n)]
    result = find(A)
    print(result)


if __name__ == "__main__":
    # 示例：运行 main，规模可按需修改
    main(5)