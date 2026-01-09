def main(n):
    # 在原程序中，n 表示人数，s 表示总数
    # 这里将输入规模参数 n 作为原程序中的 n
    # 并构造确定性的 s，令 s = n * (n // 2 + 1)
    if n <= 0:
        return 0
    people = n
    s = people * (people // 2 + 1)

    if s <= people:
        sol = 1

    else:
        sol = s // people
        if s % people:
            sol += 1

    # print(sol)
    pass
    return sol


if __name__ == "__main__":
    main(10)