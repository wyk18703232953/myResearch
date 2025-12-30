from collections import defaultdict, Counter
from random import randint

def main(n):
    # 1. 生成测试数据：规模为 n 的整数数组
    #   这里生成范围在 [0, 100] 的随机整数，你可以根据需要修改范围
    arr_list = [randint(0, 100) for _ in range(n)]
    arr = Counter(arr_list)

    ans_ = []

    # 预计算 2 的幂
    t_p = [2 ** i for i in range(31)]

    # 如果没有数据，直接返回
    if not arr:
        return

    d = defaultdict(int)
    # 初始化：至少有一个数
    m = 1
    ans_lis = [list(arr.keys())[0]]

    # 按照原逻辑枚举
    for i in arr:
        for j in t_p:
            a, b, c = i, i + j, i + 2 * j
            s = (arr[a] > 0) + (arr[b] > 0) + (arr[c] > 0)
            if s > m:
                m = s
                ans_lis = [x for x in (a, b, c) if arr[x]]

    ans_.append(m)
    t = ""
    for i in ans_lis:
        t += str(i) + " "
    ans_.append(t)

    # 输出
    for i in ans_:
        print(i)


if __name__ == "__main__":
    # 示例：运行 main，规模为 10
    main(10)