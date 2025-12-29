from random import randint

mod = 1000000007
inf = float("inf")

def permute(b, x, ind, ans):
    if ind == len(b):
        return 1
    f = 0
    for i in range(9, -1, -1):
        if x[i] > 0 and i <= int(b[ind]):
            x[i] -= 1
            ans[ind] = str(i)
            if i < int(b[ind]):
                f = 1
            if f:
                k = 9
                for j in range(ind + 1, len(b)):
                    while x[k] == 0:
                        k -= 1
                    ans[j] = str(k)
                    x[k] -= 1
                return 1
            if permute(b, x, ind + 1, ans):
                return 1
            x[i] += 1
    return 0


def solve(a, b):
    if len(str(a)) < len(str(b)):
        s = list(str(a))
        s.sort(reverse=True)
        return "".join(s)
    else:
        x = [0] * 10
        for i in str(a):
            x[int(i)] += 1
        b = str(b)
        ans = ['0'] * len(b)
        permute(b, x, 0, ans)
        return "".join(ans)


def main(n: int):
    """
    n 作为规模参数，用于控制随机生成数据的范围：
    - a, b 为 [10^(n-1), 10^n - 1] 之间的整数（n >= 1）
    """
    if n <= 0:
        n = 1
    low = 10 ** (n - 1)
    high = 10 ** n - 1
    a = randint(low, high)
    b = randint(low, high)
    result = solve(a, b)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(3) 生成 3 位数规模的随机测试数据
    main(3)