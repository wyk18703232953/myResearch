def main(n):
    # 解释：原程序结构为：
    # T = int(input())
    # 接下来 T 行，每行是一个字符串
    # 逻辑：将字符串按长度排序，然后检查每个是否为下一个的子串
    
    # 将 n 映射为字符串数量
    T = n
    if T <= 0:
        return

    # 确定性生成字符串列表
    # 构造方式：第 i 个字符串是由字符 'a' * i + 'b' 构成
    # 这样长度递增，且前缀关系明确，适合规模化并且可重复
    lis = []
    for i in range(1, T + 1):
        s = "a" * i + "b"
        lis.append(s)

    # 保持原算法逻辑
    lis = sorted(lis, key=len)

    for i in range(len(lis) - 1):
        if lis[i] not in lis[i + 1]:
            # print("NO")
            pass
            return

    # print("YES")
    pass
    for s in lis:
        # print(s)
        pass
if __name__ == "__main__":
    main(5)