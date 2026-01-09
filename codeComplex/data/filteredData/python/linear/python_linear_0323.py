def main(n):
    x = n
    list1 = [str(i) for i in range(x)]

    # 第二组输入，模拟部分重叠和不重叠的情况
    list2 = []
    for i in range(x):
        if i % 3 == 0:
            list2.append(str(i))  # 与第一组有重叠

        else:
            list2.append(str(i + x))  # 不在第一组中

    for value in list2:
        if value in list1:
            list1.remove(value)

    # print(len(list1))
    pass
if __name__ == "__main__":
    main(10)