def main(n: int):
    """
    将原程序改为可参数化的 main(n) 函数版本。
    原逻辑：给定 move, can，找 i 使得 curr-(move-i)==can，否则输出 0。
    这里根据规模 n 自动生成测试数据：
      move = n
      can  = n // 2
    """
    move = n
    can = n // 2

    curr = 0
    for i in range(1, move + 1):
        curr += i
        if curr - (move - i) == can:
            print(move - i)
            break
    else:
        print(0)


if __name__ == "__main__":
    # 示例：可根据需要修改测试规模
    main(10)