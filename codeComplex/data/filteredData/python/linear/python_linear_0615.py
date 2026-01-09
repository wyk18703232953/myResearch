def main(n):
    # 确定性生成输入数据
    # a: 1..n
    a = [i + 1 for i in range(n)]
    # b: 将 a 向右循环平移一位
    b = [a[-1]] + a[:-1] if n > 0 else []

    now = 0
    ans = []
    h = set()
    for i in range(n):
        count = 0
        while b[i] not in h:
            h.add(a[now])
            now += 1
            count += 1
        ans.append(str(count))
    # print(" ".join(ans))
    pass
if __name__ == "__main__":
    main(10)