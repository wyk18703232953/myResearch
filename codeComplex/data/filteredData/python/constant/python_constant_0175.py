def main(n):
    # 解释输入结构：原程序读取两个整数 l, r
    # 这里用 n 生成一个确定性的区间 [l, r]
    # 令 l = 1, r = n，保证规模由 n 控制
    l = 1
    r = n

    if l % 2 != 0:
        l += 1
    if l + 2 > r:
        # print(-1)
        pass

    else:
        # print(l, l + 1, l + 2)
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行时间复杂度实验
    main(10)