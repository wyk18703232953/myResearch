def main(n):
    # 生成确定性的输入数组 a，长度为 n
    # 使用简单规则：a[i] = i + 1
    a = [i + 1 for i in range(n)]

    a = sorted(a)
    ans = 0
    b = [0] * n
    for i in range(n):
        if b[i] == 0:
            ans += 1
            for j in range(i, n):
                if a[j] % a[i] == 0:
                    b[j] = 1
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做规模实验
    main(10)