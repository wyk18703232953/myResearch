import random

def main(n):
    # 生成测试数据：1..n 的一个随机排列
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    dict1 = {}
    arr1 = [0] * n

    # arr1[val-1] = 该值在数组中的下标
    for i in range(n):
        arr1[arr[i] - 1] = i

    # 初始化字典
    for i in range(n):
        dict1[i + 1] = []

    # 构建 dict1：对每个元素，以其值为步长向左右跳，看能否遇到更大的值
    for i in range(n):
        # 向左
        for j in range(i - arr[i], -1, -arr[i]):
            if arr[j] > arr[i]:
                dict1[arr[i]].append(arr[j])
        # 向右
        for j in range(i + arr[i], n, arr[i]):
            if arr[j] > arr[i]:
                dict1[arr[i]].append(arr[j])

    strarr = ['.'] * n

    # 逆序处理值从 n 到 1 对应的位置上的胜负情况
    for i in range(n - 1, -1, -1):
        cur_val = arr[arr1[i]]
        bigger_list = dict1[cur_val]

        if len(bigger_list) == 0:
            strarr[arr1[i]] = 'B'
        else:
            if len(bigger_list) == 1 and len(dict1[bigger_list[0]]) == 0:
                strarr[arr1[i]] = 'A'
            else:
                flag = 0
                for j in bigger_list:
                    # j 是值，arr1[j-1] 是 j 在原数组中的下标
                    if strarr[arr1[j - 1]] == 'B':
                        flag = 1
                        break
                if flag == 1:
                    strarr[arr1[i]] = 'A'
                else:
                    strarr[arr1[i]] = 'B'

    # 输出结果
    print("".join(strarr))


if __name__ == "__main__":
    # 示例：可以在这里调用 main 进行简单测试
    main(10)