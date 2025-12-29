from collections import Counter
import random

def get_frequency(lst):
    dic = {}
    for ele in lst:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    return dic

def main(n):
    # 生成测试数据：
    # 原代码: n, m = map(int, input().split())
    #         c = list(map(int, input().split()))
    # 逻辑只用到 n 和数组 c，与 m 无关。
    #
    # 这里我们令 m = n，并生成长度为 m 的数组 c。
    # 为了覆盖不同情况：
    # - 若 n 为偶数：生成恰好 n 个不同元素（满足 len(set(c)) == n）
    # - 若 n 为奇数：在 n 个位置中制造重复（不满足 len(set(c)) == n）
    m = n

    if n <= 1:
        # 退化规模：只有一个元素，len(set(c)) == 1 == n
        c = [1]
    elif n % 2 == 0:
        # 偶数 n：生成 n 个不同元素
        c = list(range(1, n + 1))
    else:
        # 奇数 n：生成有重复的数组
        base = list(range(1, n))  # 1..n-1 共 n-1 个不同元素
        # 再重复其中一个，使总长度为 n，但不同元素数为 n-1 < n
        c = base + [random.choice(base)]

    kk = get_frequency(c)

    if len(set(c)) == n:
        result = min(kk.values())
    else:
        result = 0

    # 输出与原程序一致的行为
    print(result)

    # 若需要调试信息，可返回中间数据
    return {
        "n": n,
        "m": m,
        "c": c,
        "frequency": kk,
        "result": result,
    }

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)