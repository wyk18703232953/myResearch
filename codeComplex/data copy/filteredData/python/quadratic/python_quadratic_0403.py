def main(n):
    # 解释：
    # 原程序输入：n, k, t
    # 这里将 n 作为字符串 t 的长度，k 固定为 3（可按需调整但需保持确定性）
    # 构造一个确定性的字符串 t：循环使用小写字母
    if n <= 0:
        return
    k = 3
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    t = "".join(alphabet[i % 26] for i in range(n))

    if n == 1:
        # print(t * k)
        pass

    else:
        i = len(t) - 1
        while i > 0 and t[-i:] != t[:i]:
            i -= 1
        t2 = t[i:]
        # print(t + t2 * (k - 1))
        pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的大小做复杂度实验
    main(10)