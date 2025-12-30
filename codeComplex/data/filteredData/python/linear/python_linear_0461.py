import random

def main(n):
    # 生成规模为 n 的随机测试数据
    # 生成 k，保证 0 <= k <= n 且 k 为偶数（因为原逻辑中使用 k//2 对括号配对）
    k = random.randrange(0, n + 1)
    if k % 2 == 1:
        k -= 1
    if k < 0:
        k = 0

    # 生成长度为 n 的随机括号串
    s = [random.choice(['(', ')']) for _ in range(n)]

    # 以下是原逻辑（去掉 input，封装到 main）
    if len(s) > k:
        p = list('(' * (k // 2))
        c = 0
        for i in range(len(s)):
            if s[i] == ')':
                p.insert(i, ')')
                c += 1
                if c == k // 2:
                    break
        print("".join(p))
    else:
        print("".join(s))


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)