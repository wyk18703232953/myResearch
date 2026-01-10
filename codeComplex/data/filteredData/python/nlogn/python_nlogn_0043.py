def main(n):
    # 生成确定性的输入数据：列表长度为 n
    # 构造规则：t[i] = (i % 3) + 1，保证有一定的重复与多样性
    t = [(i % 3) + 1 for i in range(n)]

    t.sort()

    if t[-1] == 1:
        t[-1] = 2
    else:
        t[-1] = 1
    t.sort()
    print(*t)


if __name__ == "__main__":
    main(10)