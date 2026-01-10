def main(n):
    # 生成确定性输入数据：长度为 n 的整数列表
    # 示例构造：lst[i] = (i * 2 + 3) % (n + 5) + 1 保证正整数且可扩展
    lst = [((i * 2 + 3) % (n + 5)) + 1 for i in range(n)]

    lst.sort()
    lst.reverse()
    m = 0
    for i in range(n):
        if sum(lst[:i]) > sum(lst[i:]):
            break
        else:
            m += 1
    print(m)


if __name__ == "__main__":
    main(10)