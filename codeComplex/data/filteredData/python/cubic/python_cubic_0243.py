import random

from types import GeneratorType

INF = float('inf')
mod = int(1e9) + 7


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


@bootstrap
def recur(r, g, b):
    if (r + b + g) == r or (r + b + g) == g or (r + b + g) == b:
        yield 0
        return
    if dp[r][g][b]:
        yield dp[r][g][b]
        return
    if r > 0 and g > 0:
        dp[r][g][b] = max(dp[r][g][b],
                          R[r - 1] * G[g - 1] + (yield recur(r - 1, g - 1, b)))
    if r > 0 and b > 0:
        dp[r][g][b] = max(dp[r][g][b],
                          R[r - 1] * B[b - 1] + (yield recur(r - 1, g, b - 1)))
    if b > 0 and g > 0:
        dp[r][g][b] = max(dp[r][g][b],
                          B[b - 1] * G[g - 1] + (yield recur(r, g - 1, b - 1)))
    yield dp[r][g][b]


def main(n):
    """
    n: 控制规模的参数。这里简单设定：
       r = g = b = max(1, n // 3)
    数组元素在 [1, 1000] 随机生成。
    """
    global R, G, B, dp

    # 根据 n 生成规模
    size = max(1, n // 3)
    r = g = b = size

    # 生成测试数据
    R = sorted(random.randint(1, 1000) for _ in range(r))
    G = sorted(random.randint(1, 1000) for _ in range(g))
    B = sorted(random.randint(1, 1000) for _ in range(b))

    # 初始化 DP 数组
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    # 运行原逻辑并输出结果
    ans = recur(r, g, b)
    print(ans)


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n
    main(9)