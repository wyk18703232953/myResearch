def main(n):
    # 1. 生成测试数据：长度为 n 的字符串 s
    #   这里简单生成周期为 3 的模式串，例如 n=5 -> "abcab"
    base = "abc"
    s = (base * (n // len(base) + 1))[:n]

    # 2. 固定一个 kk（原程序从输入中读取）
    #   这里设为 3，可按需要修改或在 main 参数中扩展
    kk = 3

    # 3. 原逻辑（去掉 input，直接使用 s 和 kk）
    # 原 if 条件 (s==s[::-1] or s!=s[::-1]) 恒为 True，故直接执行内部逻辑
    k = ""
    l = 0
    for i in reversed(range(1, n)):
        k = s[i] + k
        if s.startswith(k):
            l = len(k)

    ss = s[l:]
    fs = s + (ss * (kk - 1))
    # print(fs)
    pass
if __name__ == "__main__":
    # 示例调用：n 可按需要修改
    main(5)