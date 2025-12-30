import random

def main(n):
    val = 10**9

    # 生成规模为 n 的测试数据
    # 这里简单设置 m = n，arr1 中 n 个随机数，m 条随机操作
    m = n

    # 随机生成 arr1 中的 n 个整数，范围 [1, val]
    arr1 = [random.randint(1, val) for _ in range(n)]
    arr1.append(val)

    # 随机生成 m 个三元组 (x1, x2, y)
    # 为了让逻辑有机会生效，x1 多数设为 1
    operations = []
    for _ in range(m):
        x1 = 1 if random.random() < 0.7 else random.randint(1, 3)
        x2 = random.randint(1, val)
        y = random.randint(1, 100)  # y 在原逻辑中未使用，随便生成
        operations.append((x1, x2, y))

    arr2 = []
    ans = val
    finalval = 0

    arr1.sort()

    for x1, x2, y in operations:
        if x1 == 1:
            if x2 == val:
                finalval += 1
            else:
                if len(arr1) > 0 and x2 >= arr1[0]:
                    arr2.append(x2)

    arr2.sort()

    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            j += 1
        elif arr1[i] == arr2[j]:
            temp1 = len(arr2) - j
            ans = min(i + temp1, ans)
            i += 1
        else:
            temp1 = len(arr2) - j
            ans = min(i + temp1, ans)
            i += 1

    ans = min(i, ans)
    result = ans + finalval
    print(result)
    return result

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)