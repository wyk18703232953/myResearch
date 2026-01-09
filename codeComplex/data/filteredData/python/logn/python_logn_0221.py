def digisum(x: int) -> int:
    count = 0
    while x > 0:
        count += x % 10
        x //= 10
    return count


def main(n: int):
    """
    将原程序改为参数化形式：
    - n 为规模，用于生成测试数据
    - 构造一个与 n 同数量级的 s，例如 s = n // 2
    - 计算并打印原逻辑的结果
    """
    # 根据 n 生成测试数据，这里设定 s 为 n 的一半（可按需求调整生成方式）
    s = n // 2

    l, r = 1, n
    flag = 0
    cur = 0  # 防止未定义使用

    while l < r:
        m = l + (r - l) // 2
        digi_sum = digisum(m)
        num = m
        if num - digi_sum >= s:
            flag = 1
            cur = m
            r = m

        else:
            l = m + 1

        if r - l == 1:
            digi_sum = digisum(l)
            num = l
            if num - digi_sum >= s:
                flag = 1
                cur = l
                break
            digi_sum = digisum(r)
            num = r
            if num - digi_sum >= s:
                flag = 1
                cur = r
                break

    if flag == 0:
        digi_sum = digisum(l)
        num = l
        if num - digi_sum >= s:
            flag = 1
            cur = l

    if flag == 0:
        # print(0)
        pass

    else:
        # print(n - cur + 1)
        pass


# 示例：如需直接运行，可取消下面注释，并指定一个 n
# if __name__ == "__main__":
#     main(100000)