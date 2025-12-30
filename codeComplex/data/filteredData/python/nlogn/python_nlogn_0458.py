import random

def main(n):
    # 生成测试数据：n, k, arr
    # 约定：1 <= k <= n，元素为 1..10^9 的随机整数
    k = random.randint(1, n)
    arr = [random.randint(1, 10**9) for _ in range(n)]

    # 原逻辑开始
    ans = arr.copy()
    ans.sort(reverse=True)
    ans = ans[:k]
    c = k
    print(sum(ans))
    j = 0
    for i in range(n):
        if (arr[i] in ans and c != 1):
            print(i + 1 - j, end=' ')
            j = i + 1
            ans.remove(arr[i])
            c -= 1
        if (c == 1):
            print(n - j)
            break

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)