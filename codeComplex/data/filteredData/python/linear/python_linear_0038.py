import random

def main(n):
    # 参数化生成测试数据
    # 为了模拟原题意，这里随机生成 k 和数组 a
    # k 取值范围 [1, n]，a 中元素取值范围 [1, n]
    if n <= 0:
        return

    k = random.randint(1, n)
    a = [random.randint(1, n) for _ in range(n)]

    # ------- 原逻辑开始 -------
    count = 0
    b = {}
    i = -1
    for idx in range(n):
        if a[idx] in b:
            b[a[idx]] += 1
        else:
            b[a[idx]] = 1
        if b[a[idx]] == 1:
            count += 1
        if count == k:
            i = idx
            break

    if count != k:
        print("-1 -1")
        return

    j = -1
    for idx in range(n):
        if a[idx] in b:
            b[a[idx]] -= 1
        if b[a[idx]] == 0:
            j = idx
            break

    if n == 1:
        print(1, 1)
    elif n == 2 and count == 2:
        print(1, 2)
    else:
        print(j + 1, i + 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)