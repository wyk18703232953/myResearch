import random

def main(n: int):
    # 生成测试数据：随机生成合法括号序列 line，长度为 n（保证 n 为偶数）
    if n % 2 == 1:
        raise ValueError("n must be even to form a valid parentheses sequence.")

    # 简单生成一个合法括号串：n//2 个 '(' 后接 n//2 个 ')'
    # 若需更随机，可进行合法洗牌，这里保持简单且合法
    line = "(" * (n // 2) + ")" * (n // 2)

    # 生成 k：为不超过 n 的偶数，且 <= 当前括号对总数*2
    # 这里简单设定 k 为 n，本意是选取一整个合法串
    # 若想模拟原题中更一般情况，可随机生成一个不超过 n 的偶数
    k = n
    # 若要随机偶数 k，可使用如下：
    # k = random.randrange(2, n + 1, 2)

    if n == k:
        print(line)
    else:
        ans = []
        arr = list(line)

        for i in range(n):
            if len(ans) == k // 2:
                break
            if arr[i] == '(':
                ans.append(i)

        for i in range(n - 1, -1, -1):
            if len(ans) == k:
                break
            if arr[i] == ')':
                ans.append(i)

        ans.sort()
        for i in ans:
            print(arr[i], end="")


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)