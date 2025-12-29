import random

def judge(a, b):
    """
    模拟交互：
    - "? x y" 的回答规则来自原题经典交互逻辑：
      返回 '0' 表示 (a^x) < (b^y)
      返回 '1' 表示 (a^x) > (b^y)
      返回 '0' 也可用于等号情况，只要保持自洽即可。
    这里实现为：
        if (a ^ x) < (b ^ y): return '0'
        elif (a ^ x) > (b ^ y): return '1'
        else: return '0'
    """
    def ask(x, y):
        ax = a ^ x
        by = b ^ y
        if ax < by:
            return '0'
        elif ax > by:
            return '1'
        else:
            return '0'

    return ask


def solve_with_judge(ask):
    """
    将原始交互式逻辑用本地函数 ask(x, y) 替代 input/print。
    返回恢复出的 (a, b)。
    """
    ans00 = ask(0, 0)
    xr = 0
    a = 0
    b = 0
    cb = 2 ** 29
    while cb:
        ans11 = ask(xr + cb, cb)
        ans10 = ask(xr, cb)  # 原代码里再次读入 ans00 的“替身”

        if ans11 == ans00:
            ans01 = ans10
            if ans01 == '1':
                a += cb
                b += cb
        else:
            ans00 = ans10
            if ans11 == '1':
                b += cb
            else:
                a += cb
            xr += cb
        cb //= 2
    return a, b


def main(n):
    """
    参数 n 控制规模，用于生成测试数据：
    - a, b 随机生成在 [0, 2^n) 内
    - 使用本地 judge 模拟交互逻辑，调用 solve_with_judge 还原 a, b
    - 打印原始 (a, b) 和 恢复后的 (a, b)
    """
    if n <= 0 or n > 29:
        raise ValueError("n 应在 1~29 之间（原程序最高使用 2^29）。")

    max_val = 1 << n
    a = random.randrange(max_val)
    b = random.randrange(max_val)

    ask = judge(a, b)
    ra, rb = solve_with_judge(ask)

    # 输出格式可自行调整，这里展示原值与恢复值
    print("original:", a, b)
    print("recovered:", ra, rb)


if __name__ == "__main__":
    # 示例：n=10
    main(10)