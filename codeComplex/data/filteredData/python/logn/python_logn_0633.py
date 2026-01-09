def main(n: int):
    # 将 n 作为 movimentos，按规模 n 自动生成 doces_final
    # 这里构造一个相对适中的目标值，便于测试
    movimentos = n
    doces_final = n // 2  # 可根据需要调整生成规则

    left, right = 0, movimentos + 1

    while left < right - 1:
        media = (left + right) // 2
        cedidos = (media * (media + 1)) // 2
        comidos = movimentos - media
        if cedidos - comidos > doces_final:
            right = media

        else:
            left = media

    result = movimentos - left
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)