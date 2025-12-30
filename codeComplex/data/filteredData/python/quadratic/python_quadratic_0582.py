import random
import string


def solve_single_case(n, k, s):
    sf = 'RGB' * (k + 2)

    max_s = 0
    for i in range(n - k + 1):
        for j in range(3):
            count = 0
            for b in range(k):
                if sf[j + b] == s[i + b]:
                    count += 1
            if count > max_s:
                max_s = count

    return k - max_s


def main(n):
    """
    n: 规模，用来生成测试数据。
       这里假设需要处理 n 个查询，每个查询的字符串长度也为 n。
    """
    # 随机生成 query_count（也可以直接用 n 做查询数，这里保持和 n 一致）
    query_count = n

    results = []

    for _ in range(query_count):
        # 对每个查询生成字符串长度 n
        length = n

        # 生成 k，保证 1 <= k <= length
        k = random.randint(1, length)

        # 从 'R', 'G', 'B' 中随机生成一个长度为 length 的字符串
        s = ''.join(random.choice('RGB') for _ in range(length))

        ans = solve_single_case(length, k, s)
        results.append(ans)

    # 输出所有结果
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5) 生成规模为 5 的测试数据并运行
    main(5)