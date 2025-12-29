from sys import stdout

MOD = 1000000007

def main(n):
    # 1. 生成规模为 n 的测试数据
    # 这里示例：生成一个长度为 n 的01串，和 q 个区间查询
    # 你可以按需修改生成规则

    # 生成字符串 s：前一半为 '1'，后一半为 '0'
    s = '1' * (n // 2) + '0' * (n - n // 2)

    # 生成查询数 q（示例为 n 个查询）
    q = n

    # 生成区间 [x, y]：示例为一些有代表性的区间
    queries = []
    for i in range(q):
        # 示例：让区间从 1 到 min(n, i+1 + n//2)，确保合法
        x = (i % n) + 1
        y = min(n, x + n // 2)
        queries.append((x, y))

    # 2. 以下是原始逻辑，改为使用上面生成的数据

    arr = []
    count = 0
    for ch in s:
        if ch == '1':
            count += 1
        arr.append(count)

    ansarr = []
    for x, y in queries:
        if x == 1:
            total1 = arr[y - 1]
        else:
            total1 = arr[y - 1] - arr[x - 2]

        total0 = (y - x + 1 - total1)

        ans = pow(2, y - x + 1, MOD) % MOD
        ans = (ans - pow(2, total0, MOD) % MOD) % MOD
        ans = (ans + MOD) % MOD

        ansarr.append(ans)

    stdout.write('\n'.join(map(str, ansarr)))


# 示例调用
if __name__ == "__main__":
    # 将 10 换成任意想要的规模 n
    main(10)