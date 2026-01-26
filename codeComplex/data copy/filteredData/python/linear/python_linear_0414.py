def main(n):
    # 解释输入结构：
    # 原程序输入为：第一行两个整数 n, k；第二行为长度为 n 的字符串 s（小写字母）
    # 这里的 main(n) 中的 n 作为字符串长度使用
    #
    # 数据生成设计（确定性）：
    # - 字符串 s：前 n 个小写字母循环生成，例如 n=1..: "abcabc..."
    # - k：与规模相关联，设定为 min(10, max(1, n // 5))，随 n 单调非降
    #
    # 这样：
    # - 字符串长度随 n 线性增长，便于时间复杂度实验
    # - k 随 n 变化但有上界，避免过大导致算法行为退化为常量

    if n <= 0:
        # 对非正规模给出一个简单的退化调用
        # print(-1)
        pass
        return

    # 生成确定性的字符串 s，长度为 n，由 'a'..'z' 循环组成
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(alphabet[i % 26] for i in range(n))

    # 生成确定性的 k，与 n 相关
    k = n // 5
    if k < 1:
        k = 1
    if k > 10:
        k = 10

    # 核心算法与原程序保持一致
    l = []
    for ch in s:
        val = ord(ch) - 96
        if val not in l:
            l.append(val)
    l.sort()
    c = l[0]
    a = 1
    b = l[0]
    for i in range(1, len(l)):
        if a == k:
            break
        if (l[i] - b) > 1:
            a += 1
            c += l[i]
            b = l[i]
    if a < k:
        # print(-1)
        pass

    else:
        # print(c)
        pass
if __name__ == "__main__":
    # 示例：使用若干不同规模调用以便实验
    for size in (5, 10, 50, 100):
        main(size)