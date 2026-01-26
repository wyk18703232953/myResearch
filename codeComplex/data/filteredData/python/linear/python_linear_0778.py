import math

def func(a, k):
    if a % k != 0:
        mod = 1

    else:
        mod = 0
    return math.floor(a / k) * k + mod * k

def core_algorithm(arr, k):
    temp = k
    answer = 0
    c = 0
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
            if check is 'true':
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
            elif check is 'false':
                temp = temp + func(int(arr[i]) - temp, k)
                if arr[i] - c <= temp and used == 0:
                    c += 1
                    check = 'true'
                    used = 1

    return answer if check is 'false' else answer + 1

def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # 映射输入结构：
    # 原程序结构为：n, m, k + 一行含 m 个整数的列表
    # 这里将：
    #   m = n
    #   k = max(1, n // 3)
    #   列表长度 = m
    #   列表元素为确定性构造：arr[i] = (i * k) // 2 + (i % (k + 1))
    m = n
    k = max(1, n // 3)

    arr = [(i * k) // 2 + (i % (k + 1)) for i in range(m)]

    result = core_algorithm(arr, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行复杂度实验
    main(10)