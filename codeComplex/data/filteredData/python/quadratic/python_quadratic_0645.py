mod = 10**9 + 7

def main(n):
    # 生成规模为 n 的确定性输入
    # 原程序结构：
    # n: 一个整数
    # a: n 个整数
    # 这里令 a[i] = (i + 1) % (n // 3 + 2) + 1，确保有重复与可整除关系
    if n <= 0:
        return 0
    a = [((i + 1) % (n // 3 + 2)) + 1 for i in range(n)]

    from collections import defaultdict as dd

    b = sorted(a)
    c = dd(int)

    ans = 0
    val = 0
    for i in range(n):
        if c[b[i]] == 0:
            val += 1
            for j in range(n):
                if b[j] % b[i] == 0:
                    c[b[j]] = val

    for x in c:
        ans = max(ans, c[x])

    # print(ans)
    pass
    return ans

if __name__ == "__main__":
    # 示例调用，可按需要修改 n 的大小做复杂度实验
    main(6)