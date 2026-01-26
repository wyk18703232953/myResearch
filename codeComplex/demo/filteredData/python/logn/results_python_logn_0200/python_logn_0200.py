def main(n):
    # 为了保持原始程序结构，这里将 s 作为规模 n 的函数确定性生成
    # 例如：s = max(1, n // 2)
    s = max(1, n // 2)

    c = 0
    last_i = s

    upper = min(s + 1000, n + 1)
    for i in range(s, upper):
        if i - sum(map(int, str(i))) >= s:
            c += 1
        last_i = i
    c += max(0, n - last_i)
    return c

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行规模实验
    result = main(10**6)
    # print(result)
    pass