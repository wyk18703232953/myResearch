def main(n: int):
    # 1) 生成测试数据
    # 将原先的输入 arr = [k_hodov, konf]
    # 简单设定：k_hodov = n，konf = n // 2
    k_hodov = n
    konf = n // 2

    # 2) 原逻辑（去除 input）
    left = 0
    right = k_hodov + 100
    while (right - left) > 1:
        mid = (right + left) // 2
        k_give = k_hodov - mid
        if ((k_give + 1) * (k_give / 2)) // 1 - mid < konf or k_give < 0:
            right = mid
        else:
            left = mid

    k_give = k_hodov - left
    if ((k_give + 1) * (k_give / 2)) // 1 - left == konf:
        print(left)
    else:
        print(left - 1)


if __name__ == "__main__":
    # 示例运行
    main(10)