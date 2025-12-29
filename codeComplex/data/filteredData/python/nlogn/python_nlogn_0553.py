import random

def main(n):
    # 生成测试数据：ll 为 1..n 的随机排列
    ll = list(range(1, n + 1))
    random.shuffle(ll)

    # 原始逻辑开始
    l = [-1 for _ in range(n + 1)]
    for i in range(n):
        j = ll[i]
        l[j] = i

    res = ["." for _ in range(n + 1)]
    res[n] = "B"

    for i in range(n - 1, 0, -1):
        toadd = "B"
        pos = l[i] % i
        while pos < n:
            j = ll[pos]
            if j <= i:
                pos += i
                continue
            if abs(l[i] - l[j]) % i == 0 and res[j] == "B":
                toadd = "A"
                break
            pos += i
        res[i] = toadd

    # 输出结果
    for i in ll:
        print(res[i], end="")
    print("")

if __name__ == "__main__":
    # 示例：运行规模为 n=10 的测试
    main(10)