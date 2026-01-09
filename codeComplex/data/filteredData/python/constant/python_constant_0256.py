def main(n):
    # 解释输入结构：
    # 原程序读取：n, pos, l, r
    # 在这里我们用传入的 n 作为“原 n”，并且确定性地构造 pos, l, r
    original_n = n

    # 将 pos 放在中间位置（偏左），l 在靠前位置，r 在靠后位置，保证覆盖一般情况
    pos = original_n // 2 + 1 if original_n > 1 else 1
    l = max(1, original_n // 4)
    r = min(original_n, 3 * original_n // 4 + 1)

    # 保证区间合法且有意义
    if l > r:
        l, r = r, l
    if l < 1:
        l = 1
    if r > original_n:
        r = original_n

    if l == 1 and r == original_n:
        result = 0
    elif l == 1 and r != original_n:
        result = abs(pos - r) + 1
    elif l != 1 and r == original_n:
        result = abs(pos - l) + 1

    else:
        result = r - l + 2 + min(abs(pos - l), abs(pos - r))

    # print(result)
    pass
if __name__ == "__main__":
    main(10)