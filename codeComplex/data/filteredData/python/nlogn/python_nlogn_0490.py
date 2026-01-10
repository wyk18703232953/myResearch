from collections import Counter

def main(n):
    # 构造确定性输入规模
    # 原程序结构：
    # n, m
    # 接着 m 个整数
    m = n * 3 if n > 0 else 0

    # 生成确定性数组：包含 0..n-1 的循环模式
    arr = [i % n if n > 0 else 0 for i in range(m)]

    # 原逻辑开始
    a = Counter(arr).values()
    i = 1
    while sum(x // i for x in a) >= n:
        i += 1
    result = i - 1
    print(result)
    return result

if __name__ == "__main__":
    main(10)