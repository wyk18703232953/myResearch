from random import randint

def main(n):
    # 生成测试数据
    # n: 数组长度
    # 生成 1 <= k <= n
    k = randint(1, n)
    # arr1: 随机整数，例如 1~10
    arr1 = [randint(1, 10) for _ in range(n)]
    # arr2: 随机 0/1
    arr2 = [randint(0, 1) for _ in range(n)]

    # 原始逻辑开始
    ans = 0
    new_arr = [0] * n

    for i in range(n):
        if arr2[i] == 0:
            new_arr[i] = arr1[i]
        else:
            ans += arr1[i]

    total = sum(new_arr[:k])
    mx = total

    j = 0
    for i in range(k, n):
        total -= new_arr[j]
        total += new_arr[i]
        if total > mx:
            mx = total
        j += 1

    result = mx + ans

    # 输出结果
    print(result)
    # 如需调试，可以打印测试数据：
    # print("n =", n, "k =", k)
    # print("arr1 =", arr1)
    # print("arr2 =", arr2)
    return result

# 示例：运行 main(10)
if __name__ == "__main__":
    main(10)