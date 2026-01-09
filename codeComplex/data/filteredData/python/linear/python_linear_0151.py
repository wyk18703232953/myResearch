def main(n):
    # 映射：原程序中数组长度 = n，p 为一个与 n 有关的确定性值
    # 这里设定 p = n + 2，以保证 p > 1 且随规模线性变化
    p = n + 2 if n > 0 else 2

    # 构造确定性数组 a，元素大小与 p 相关
    # 使用简单算术构造：a[i] = (i * i + 3 * i + 1) % (2 * p)
    a = [((i * i + 3 * i + 1) % (2 * p)) for i in range(n)]

    a = [c % p for c in a]
    s = sum(a)
    sp = s % p
    if sp == s or sp + 1 == p:
        # print(sp)
        pass

    else:
        # print(sp + p)
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 来做规模实验
    main(10)