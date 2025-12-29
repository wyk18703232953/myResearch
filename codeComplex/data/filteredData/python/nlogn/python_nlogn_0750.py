import random

def main(n: int):
    # 1. 生成测试数据：生成一个长度为 n 的非负整数数组
    # 可以根据需要调整数据范围，这里用 0~10^9
    arr = [random.randint(0, 10**9) for _ in range(n)]

    arr.sort()
    if n >= 2 and arr[0] == arr[1] == 0:
        print("cslnb")
        return
    else:
        flag = 0
        for i in range(n - 2):
            if arr[i] == arr[i + 1] == arr[i + 2]:
                flag = 1
                break
        if flag == 1:
            print("cslnb")
            return
        else:
            flag = 0
            ind = 0
            for i in range(n - 1):
                if arr[i] == arr[i + 1]:
                    ind = i
                    flag += 1
            if flag == 1 and ind > 0 and arr[ind - 1] == arr[ind] - 1:
                print("cslnb")
                return
            elif flag >= 2:
                print("cslnb")
                return
            else:
                safe = 0
                for i in range(n):
                    if arr[i] - i >= 0:
                        safe += arr[i] - i
                if safe % 2 == 0:
                    print("cslnb")
                else:
                    print("sjfnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)