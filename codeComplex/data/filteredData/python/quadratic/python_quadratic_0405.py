def main(n: int) -> str:
    # 生成测试数据：使用前 n 个小写字母循环构造字符串
    base = "abcdefghijklmnopqrstuvwxyz"
    if n <= 0:
        t = ""
    else:
        t = (base * ((n + len(base) - 1) // len(base)))[:n]

    k = 3  # 可按需要修改测试重复次数

    # 以下是原 solve() 逻辑（去掉 input，使用生成的 t 和固定 k）
    t_str = t
    j = 0
    for i in range(1, n):
        if t_str[:i] == t_str[-i:]:
            j = i
    s = t_str + (k - 1) * t_str[-(n - j):]
    return s


if __name__ == "__main__":
    # 简单示例：n = 5
    print(main(5))