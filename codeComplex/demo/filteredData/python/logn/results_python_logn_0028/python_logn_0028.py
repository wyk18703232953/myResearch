def has(x, bit):
    return x & (1 << bit)

def main(n: int):
    """
    用 n 生成输入 (l, r)，并执行原 solve() 的逻辑。
    返回计算结果，便于做性能测试/曲线拟合。
    """

    # --------- n -> (l, r) 的确定性构造（你可以按需求改）---------
    # 目标：保证 l <= r，且规模随 n 增大而增大
    # 这里用一个简单构造：l = n, r = 2n + n//2
    l = n
    r = 2 * n + (n // 2)
    if l > r:
        l, r = r, l
    # ------------------------------------------------------------

    bit = 62
    while bit >= 0 and has(l, bit) == has(r, bit):
        bit -= 1

    ans = (1 << (bit + 1)) - 1   # 等价于 2**(bit+1)-1，但用位运算更常见
    return ans


if __name__ == "__main__":
    # 示例：你原来是读一组 l,r；现在改为给 main 传 n
    # 你可以在你的实验框架里循环调用 main(n)
    print(main(10))