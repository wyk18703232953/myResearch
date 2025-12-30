import random

def main(n: int):
    # 生成测试数据：长度为 n 的二进制字符串
    # 可根据需要调整生成规则
    s1 = ''.join(random.choice('01') for _ in range(n))
    s2 = ''.join(random.choice('01') for _ in range(n))

    arr1 = s1.encode()
    arr2 = s2.encode()
    arr1 = bytearray(arr1)
    arr2 = bytearray(arr2)

    tot = 0
    for i in range(n - 1):
        if arr1[i] == 48 and arr1[i + 1] == 48 and arr2[i] == 48:
            tot += 1
            arr1[i] = 49
            arr1[i + 1] = 49
            arr2[i] = 49
        elif arr1[i] == 48 and arr2[i] == 48 and arr2[i + 1] == 48:
            tot += 1
            arr1[i] = 49
            arr2[i] = 49
            arr2[i + 1] = 49
        elif arr2[i] == 48 and arr2[i + 1] == 48 and arr1[i + 1] == 48:
            tot += 1
            arr2[i] = 49
            arr2[i + 1] = 49
            arr1[i + 1] = 49
        elif arr1[i] == 48 and arr1[i + 1] == 48 and arr2[i + 1] == 48:
            tot += 1
            arr1[i] = 49
            arr1[i + 1] = 49
            arr2[i + 1] = 49

    print(tot)


if __name__ == "__main__":
    # 示例调用：规模 n=10
    main(10)