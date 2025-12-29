import random

def main(n: int):
    # 1. 生成测试数据
    # 约定：k <= n，arr 中元素为 1..10^9 的随机整数
    k = random.randint(1, n)
    arr = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 原逻辑开始
    new = []
    ans = 0
    for i in range(n):
        new.append((arr[i], i))
    new.sort(reverse=True)
    check = [0] * n
    for i in range(k):
        ans += new[i][0]
        check[new[i][1]] = 1
    count = 0
    res = []
    for i in range(n):
        if check[i] == 1:
            count += 1
            res.append(count)
            count = 0
        else:
            count += 1
    res[-1] += count

    # 3. 输出
    print(ans)
    print(*res)


if __name__ == '__main__':
    # 示例：调用 main，n 可按需修改
    main(10)