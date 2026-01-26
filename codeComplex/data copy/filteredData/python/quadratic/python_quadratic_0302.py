def main(n):
    # n 表示列表长度
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成输入列表 t：简单递增序列
    t = [i % 10 for i in range(1, n + 1)]

    sw = 0

    # 保持原逻辑：每次在 t[1:] 中寻找与 t[0] 相同的元素，计算位置并重构列表
    while t != []:
        if len(t) == 1:
            # 原代码在这种情况下会抛出异常，这里保证逻辑可运行
            t = []
            break
        # 查找 t[0] 在 t[1:] 中的第一次出现位置
        try:
            pr = 1 + t[1:].index(t[0])
        except ValueError:
            # 若未找到，则结束循环（与原逻辑尽可能接近而不报错）
            break
        sw += pr - 1
        t = t[1:pr] + t[pr + 1:]

    # print(sw)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值
    main(10)