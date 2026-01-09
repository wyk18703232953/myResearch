def main(n: int):
    # 根据规模 n 生成测试数据
    # 约定：left = n，right = 2 * n，且保证 left <= right
    left = n
    right = 2 * n

    if left == right:
        # print(0)
        pass

    else:
        x = 1
        while x <= right:
            x *= 2
        x //= 2
        y = x
        # 原代码逻辑：while y > 0 and (x <= left or x > right)
        while y > 0 and (x <= left or x > right):
            if x <= left:
                x += y

            else:
                x -= y
            y //= 2
        # print(x ^ (x - 1))
        pass
if __name__ == "__main__":
    # 示例：调用 main，n 可自行修改
    main(10)