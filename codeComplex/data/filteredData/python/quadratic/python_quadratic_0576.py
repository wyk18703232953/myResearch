import random

def solve_single_case(n, k, s):
    ans = k
    sample = "RGB"
    for i in range(n - k + 1):
        # pattern starting with 'R'
        cnt = 0
        x = 0
        for j in range(i, i + k):
            if s[j] != sample[x]:
                cnt += 1
            x = (x + 1) % 3
        ans = min(ans, cnt)

        # pattern starting with 'G'
        cnt = 0
        x = 1
        for j in range(i, i + k):
            if s[j] != sample[x]:
                cnt += 1
            x = (x + 1) % 3
        ans = min(ans, cnt)

        # pattern starting with 'B'
        cnt = 0
        x = 2
        for j in range(i, i + k):
            if s[j] != sample[x]:
                cnt += 1
            x = (x + 1) % 3
        ans = min(ans, cnt)
    return ans


def main(n):
    # 生成 q 个测试用例，这里令 q = n
    q = n
    results = []

    for _ in range(q):
        # 对每个用例：
        # 1. 随机生成长度为 n 的字符串 s（字符来自 R/G/B）
        # 2. 随机生成 1 <= k <= n
        k = random.randint(1, n)
        s = ''.join(random.choice('RGB') for _ in range(n))
        res = solve_single_case(n, k, s)
        results.append(res)

    # 为了与原程序行为类似，这里只输出最后一个测试用例的结果
    # 如果需要查看所有结果，可改成打印 results
    print(results[-1])


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)