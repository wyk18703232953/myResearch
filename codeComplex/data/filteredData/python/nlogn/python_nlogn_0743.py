def main(n):
    # n 表示数组长度
    # 构造一个确定性的数组：示例为 [0, 1, 2, ..., n-1]
    # 可按需要调整构造方式，如包含重复或更复杂结构
    arr = [i // 2 for i in range(n)]

    arr.sort()
    ans = 0
    mark = 0
    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 1] == arr[i + 2]:
            # print('cslnb')
            pass
            return
        elif arr[i + 1] == arr[i + 2] and arr[i] + 1 == arr[i + 1]:
            # print('cslnb')
            pass
            return

    countcopy = 0
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1] and arr[i] == 0:
            # print('cslnb')
            pass
            return
        if arr[i] == arr[i + 1]:
            countcopy += 1
    if countcopy > 1:
        # print('cslnb')
        pass
        return

    for i in range(len(arr)):
        if arr[i] >= mark:
            ans += (arr[i] - mark)
            mark += 1

    if ans % 2 == 0:
        # print('cslnb')
        pass

    else:
        # print('sjfnb')
        pass
if __name__ == "__main__":
    main(10)