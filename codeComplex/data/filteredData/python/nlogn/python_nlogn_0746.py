import random

def main(n: int):
    # 生成测试数据：n 个非负整数
    # 可根据需求调整数据范围
    arr = [random.randint(0, 10**9) for _ in range(n)]

    tmp = 0
    for i in range(len(arr)):
        tmp += (arr[i] - i)

    arr.sort()
    c = 0
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            c += 1
        if i != 1 and arr[i] == arr[i - 1] and arr[i - 1] == arr[i - 2] + 1:
            print("cslnb")
            return

    if c > 1 or (len(arr) >= 2 and arr[0] == arr[1] == 0):
        print("cslnb")
        return

    print("cslnb" if tmp % 2 == 0 else "sjfnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)