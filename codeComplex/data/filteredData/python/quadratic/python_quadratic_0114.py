def main(n):
    # 映射：原代码有两个整数 n, m 和一个长度为 m 的序列 c
    # 这里用传入的 n 作为原来的 n，同时构造一个确定性的 m 和序列 c
    original_n = n
    if original_n <= 0:
        # print(0)
        pass
        return

    # 构造一个确定性的 m（至少为 1）
    m = max(1, original_n * 3)

    # 构造长度为 m 的序列 c，元素范围为 [1, original_n]
    c = [(i % original_n) + 1 for i in range(m)]

    aa = [0] * (original_n + 1)
    for cc in c:
        aa[cc] += 1
    # print(min(aa[1:]))
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模
    main(10)