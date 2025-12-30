import math
import random

def func(a, k):
    if a % k != 0:
        mod = 1
    else:
        mod = 0
    return math.floor(a / k) * k + mod * k

def main(n):
    # 生成测试数据
    # n: 列表长度
    # 随机生成 m, k 和列表内容
    m = random.randint(1, 10**9)
    k = random.randint(1, 10**5) or 1  # 避免 k 为 0
    arr = [random.randint(1, 10**9) for _ in range(n)]

    temp = k
    size = 0
    answer = 0
    c = 0
    c2 = 0
    check = 'false'
    used = 0

    temp = func(int(arr[0]), k)
    for i in range(len(arr)):
        arr[i] = int(arr[i])
        used = 0
        if arr[i] <= temp:
            c += 1
            check = 'true'
            used = 1
        if arr[i] >= temp:
            if check == 'true':
                answer += 1
                check = 'false'
                temp += c
                c = 0
                if arr[i] - c <= temp and used == 0:
                    c += 1
                    check = 'true'
                    used = 1
                else:
                    temp = temp + func(int(arr[i]) - temp, k)
                    if arr[i] - c <= temp and used == 0:
                        c += 1
                        check = 'true'
                        used = 1
            elif check == 'false':
                temp = temp + func(int(arr[i]) - temp, k)
                if arr[i] - c <= temp and used == 0:
                    c += 1
                    check = 'true'
                    used = 1

    result = answer if check == 'false' else answer + 1
    print(result)
    return result

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)