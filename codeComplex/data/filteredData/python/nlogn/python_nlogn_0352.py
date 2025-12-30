from collections import Counter
from random import randint

def main(n):
    # 1. 生成测试数据：长度为 n 的整数数组
    #   这里生成范围在 [-10^6, 10^6] 的随机整数
    #   如需固定数据，可自行改写为指定列表
    arr_list = [randint(-10**6, 10**6) for _ in range(n)]

    # 2. 将原逻辑封装起来
    t_p = [2 ** i for i in range(31)]
    arr = Counter(arr_list)

    ans_ = []
    d = {}  # 原代码中 d 未使用，这里保留形式
    # 初始最大出现次数 m
    # 若 arr 为空，则直接输出 0 和空行
    if not arr:
        ans_.append(0)
        ans_.append("")
        for x in ans_:
            print(x)
        return

    m = 1
    ans_lis = [[list(arr.keys())[0], 1]]

    for i in arr:
        for j in t_p:
            a, b, c = i, i + j, i + 2 * j
            s = arr[a] + arr[b] + arr[c]
            if s > m:
                m = s
                ans_lis = [[x, arr[x]] for x in [a, b, c]]

    ans_.append(m)
    t = ""
    for val, cnt in ans_lis:
        t += (str(val) + " ") * cnt
    ans_.append(t.strip())

    for x in ans_:
        print(x)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)