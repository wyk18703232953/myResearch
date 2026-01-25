def main(n):
    # 固定 x，使行为仅由 n 决定
    x = 7

    # 生成确定性的输入集合 a，规模为 n
    # 使用简单算术构造：i, i+1 等，保证重复元素可被 set 去重
    # 为了更贴近原始语义，先生成长度为 n 的列表，再转为 set
    base_list = [(i * 2 + 3) for i in range(n)]
    a = set(base_list)

    if len(a) < n:
        print(0)
    else:
        d = set()
        p = 0
        for i in a:
            val = i & x
            d.add(val)
            if val != i and val in a:
                print(1)
                p = 1
                break
        if len(d) < n and p == 0:
            print(2)
        elif p != 1:
            print(-1)


if __name__ == "__main__":
    # 示例调用：可按需修改 n 的值进行规模实验
    main(10)