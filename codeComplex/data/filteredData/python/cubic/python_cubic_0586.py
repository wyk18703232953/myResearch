import random

def main(n: int):
    # 1. 生成测试数据
    # 生成一个长度为 n 的数字串 a（允许前导零）
    a = [str(random.randint(0, 9)) for _ in range(n)]
    # 生成一个上界 b，使得 b 的位数大致在 [n, n+1] 范围内
    b_len = max(1, n + random.randint(0, 1))
    b_digits = [str(random.randint(0, 9)) for _ in range(b_len)]
    # 最高位不能为 0（避免太小）
    if b_digits[0] == '0':
        b_digits[0] = str(random.randint(1, 9))
    b = int(''.join(b_digits))

    # 2. 原始逻辑
    a.sort(reverse=True)
    ans = ''
    while len(a) > 0:
        for i in range(len(a)):
            tmp = ans + a[i] + ''.join(sorted(a[:i] + a[i + 1:]))
            if int(tmp) <= b:
                ans += a[i]
                a = a[:i] + a[i + 1:]
                break

    print(ans)

if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)