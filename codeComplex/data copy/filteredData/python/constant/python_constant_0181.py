def main(n):
    # 映射：用 n 生成 l 和 r，保证可规模化且确定性
    # 令区间长度为 n+2，起点随 n 变化
    l = n
    r = l + n + 1

    if l == r or l + 1 == r:
        # print(-1)
        pass
    elif l % 2 == 0:
        # print(l, l + 1, l + 2)
        pass
    elif l % 2 != 0 and r - l + 1 > 3:
        # print(l + 1, l + 2, l + 3)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # 示例：可修改 n 进行不同规模实验
    main(10)