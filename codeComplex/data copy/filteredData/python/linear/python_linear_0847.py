def main(n):
    # 生成确定性测试数据：长度为 n 的整数数组
    # 使用简单的算术构造，保证可重复性
    arr = [((i * 7 + 3) % (n + 5)) for i in range(n)] if n > 0 else []
    if not arr:
        # print("NO")
        pass
        return

    maxval = max(arr)
    maxindex = -1
    for i in range(n):
        if arr[i] == maxval:
            maxindex = i
            break

    flag = 0
    temp = maxval
    for i in range(maxindex - 1, -1, -1):
        if temp <= arr[i]:
            flag = 1
            break

        else:
            temp = arr[i]

    temp = maxval
    for i in range(maxindex + 1, n):
        if arr[i] >= temp:
            flag = 1
            break

        else:
            temp = arr[i]

    if flag == 0:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小
    main(10)