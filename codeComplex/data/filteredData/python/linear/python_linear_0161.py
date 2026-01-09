def main(n):
    # n 表示输入规模，即序列长度
    E = [(i * 7 + 3) % (n // 2 + 1) for i in range(n)]
    D = {}
    for e in E:
        D[e] = D.get(e, 0) + 1
    for e in E:
        # print(D[e])
        pass
if __name__ == "__main__":
    main(10)