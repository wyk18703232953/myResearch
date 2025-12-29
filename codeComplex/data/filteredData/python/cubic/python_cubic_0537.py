success = 0

def solve(b, freq, i, n, res):
    global success
    if i == len(b):
        success = res
    else:
        success = 0
        move = 9
        while move >= 0 and success == 0:
            m = int(b[i])
            if freq[move] > 0 and res * 10 + move <= n * 10 + m:
                res = res * 10 + move
                n = n * 10 + m
                freq[move] -= 1
                if solve(b, freq, i + 1, n, res) == 0:
                    res //= 10
                    n //= 10
                    freq[move] += 1
            move -= 1
    return success

def main(n):
    # 生成测试数据：
    # a 为一个由 0-9 组成的长度为 n 的数字串（允许前导 0）
    # b 为一个长度为 n 或 n+1 的数字串，这里简单生成比 a 大一位的上界数字串
    import random

    # 生成 a: 长度为 n
    a_digits = [str(random.randint(0, 9)) for _ in range(n)]
    a = ''.join(a_digits)

    # 生成 b: 若 len(b) > len(a)，则触发简单分支；否则走回溯分支
    # 这里生成长度为 n 或 n+1 的 b
    if random.random() < 0.5:
        # 长度为 n+1，确保 len(b) > len(a)
        b_len = n + 1
    else:
        # 长度为 n
        b_len = n

    # 生成 b 为某个随机数字串
    b_digits = [str(random.randint(0, 9)) for _ in range(b_len)]
    b = ''.join(b_digits)

    # 以下为原逻辑
    global success
    success = 0

    freq = [0] * 10
    v = []
    for x in a:
        d = int(x)
        v.append(d)
        freq[d] += 1
    v.sort()

    if len(b) > len(a):
        ans = 0
        m = 1
        for x in v:
            ans = x * m + ans
            m *= 10
    else:
        ans = solve(b, freq, 0, 0, 0)

    print(ans)

if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)