def main(n):
    # 生成确定性输入数据
    # a: 长度 n 的排列（0..n-1 的简单“洗牌”）
    a = [(i * 3 + 1) % n for i in range(n)]
    # b: 长度 n 的排列（0..n-1 的另一种顺序）
    b = [(i * 5 + 2) % n for i in range(n)]

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