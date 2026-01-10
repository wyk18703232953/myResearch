def gC(m, a, n):
    s = [0 for _ in range(2 * n + 1)]
    cur = n
    res = 0
    s[cur] = 1
    ad = 0
    for i in range(n):
        if a[i] < m:
            cur -= 1
            ad -= s[cur]
        else:
            ad += s[cur]
            cur += 1
        res += ad
        s[cur] += 1
    return res

def main(n):
    # n 表示数组长度
    if n <= 0:
        return 0
    # 确定性构造 m 和数组 a
    m = n // 2 + 1
    a = [(i * 2 + 3) % (n + 5) for i in range(n)]
    result = gC(m, a, n) - gC(m + 1, a, n)
    return result

if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的大小进行实验
    print(main(10))