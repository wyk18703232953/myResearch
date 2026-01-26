def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组
    # 这里选择 arr[i] = i+1，保证有序且无重复，便于时间复杂度实验
    arr = [i + 1 for i in range(n)]
    color = [0] * n
    arr.sort()

    ans = 0
    for i in range(n):
        if color[i]:
            continue
        ans += 1
        for j in range(i, n):
            if arr[j] % arr[i] == 0:
                color[j] = ans

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模做时间复杂度实验
    main(10)