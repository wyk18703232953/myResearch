import random

def main(n):
    # 1. 生成规模为 n 的测试数据：非负整数数组
    #    这里生成 0~n 之间的随机数，包含重复
    arr = [random.randint(0, n) for _ in range(n)]

    arr.sort()
    ans = 0
    mark = 0

    # 对应原始代码的判定逻辑
    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 1] == arr[i + 2]:
            print('cslnb')
            return
        elif arr[i + 1] == arr[i + 2] and arr[i] + 1 == arr[i + 1]:
            print('cslnb')
            return

    countcopy = 0
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1] and arr[i] == 0:
            print('cslnb')
            return
        if arr[i] == arr[i + 1]:
            countcopy += 1
    if countcopy > 1:
        print('cslnb')
        return

    for i in range(len(arr)):
        if arr[i] >= mark:
            ans += (arr[i] - mark)
            mark += 1

    if ans % 2 == 0:
        print('cslnb')
    else:
        print('sjfnb')


# 示例调用
if __name__ == "__main__":
    main(5)