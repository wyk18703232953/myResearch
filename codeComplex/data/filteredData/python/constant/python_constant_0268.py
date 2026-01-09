def main(n: int) -> int:
    """
    n: 规模参数，这里我们按如下方式生成测试数据：
       pos 固定为中间位置 n//2（至少为 1，至多为 n）
       l  固定为 1
       r  固定为 n
    返回：计算得到的 step 值
    """
    # 生成测试数据
    pos = max(1, min(n, n // 2))  # 保证在 [1, n] 之间
    l = 1
    r = n

    step = 0
    dif = lambda a, b: abs(a - b)

    if dif(pos, l) < dif(pos, r):
        if l != 1:
            step += dif(pos, l) + 1
            pos = l
        if r != n:
            step += dif(pos, r) + 1

    else:
        if r != n:
            step += dif(pos, r) + 1
            pos = r
        if l != 1:
            step += dif(pos, l) + 1

    return step


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需要修改 n
    # print(main(10))
    pass