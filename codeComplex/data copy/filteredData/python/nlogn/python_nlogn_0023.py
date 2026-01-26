def main(n):
    # 生成确定性输入数据：列表长度为 n
    # 构造方式：l[i] = (i // 2) 用于保证有重复且有可能存在严格大于最小值的元素
    l = [(i // 2) for i in range(n)]
    l.sort()
    for x in range(1, n):
        if l[x] > l[0]:
            # print(l[x])
            pass
            break

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)