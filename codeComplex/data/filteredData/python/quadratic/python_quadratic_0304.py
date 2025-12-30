import random

def main(n: int):
    # 生成测试数据：a 是长度为 2n 的数组，每个 1..n 出现两次，随机打乱
    a = list(range(1, n + 1)) * 2
    random.shuffle(a)

    l = [-1] * n
    r = [-1] * n

    for i in range(2 * n):
        x = a[i] - 1
        if l[x] == -1:
            l[x] = i
        r[x] = i

    ans = 0
    for i in range(n):
        for j in range(n):
            if l[i] < l[j] < r[j] < r[i]:
                ans += 2
    for i in range(n):
        ans += r[i] - l[i] - 1

    print(ans // 2)

if __name__ == "__main__":
    # 示例：可根据需要修改 n 的值
    main(5)