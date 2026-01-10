def main(n):
    # n 表示数组长度
    list1 = [(i * 3 + 1) % (2 * n + 1) + 1 for i in range(n)]
    sum2 = 0
    sum1 = 0
    count = 0
    list1.sort(reverse=True)
    for i in range(len(list1)):
        sum1 = sum1 + list1[i]
    for i in range(len(list1)):
        if int(sum1 / 2) >= sum2:
            sum2 = sum2 + list1[i]
            count = count + 1
    print(count)


if __name__ == "__main__":
    main(10)