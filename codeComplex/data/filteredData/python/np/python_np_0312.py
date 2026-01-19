def main(n):
    # 映射输入结构：原程序有两个整数 n, k
    # 这里用 n 作为规模，并确定性地生成 k
    # 例如令 k = n，且至少为 1
    k = max(1, n)

    same = [0] * (k + 1)
    diff = [0] * (k + 1)
    same[1] = 2
    if k > 1:
        diff[2] = 2
    for _ in range(n - 1):
        newsame = [0] * (k + 1)
        newdiff = [0] * (k + 1)
        for i in range(1, k + 1):
            newsame[i] = (same[i] + same[i - 1] + 2 * diff[i]) % 998244353
        for i in range(2, k + 1):
            newdiff[i] = (2 * same[i - 1] + diff[i] + diff[i - 2]) % 998244353
        same = newsame
        diff = newdiff
    return (same[-1] + diff[-1]) % 998244353


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    result = main(10)
    print(result)