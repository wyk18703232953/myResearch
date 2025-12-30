import random

def socket(n, m, k, arr):
    arr.sort(reverse=True)
    devices = m
    curr_socket = 0
    e_socket = k
    i = 0
    t_socket = 0
    count = 0
    while i < n:
        if e_socket >= devices:
            return 0
        if curr_socket == 0:
            curr_socket += arr[i]
            count += 1
            e_socket -= 1
            t_socket = curr_socket + e_socket
        else:
            if t_socket >= devices:
                return count
            else:
                curr_socket += arr[i] - 1
                count += 1
                t_socket = curr_socket + e_socket
        i += 1
    if t_socket >= devices:
        return count
    return -1

def main(n):
    # 生成测试数据
    # 设定 m 和 k 与 n 同量级，且保证有一定概率可行
    # m: 需要连接的设备数，范围 [1, 3n]
    # k: 初始空插座数，范围 [0, n]
    m = random.randint(1, max(1, 3 * n))
    k = random.randint(0, max(0, n))

    # 每个插线板可以提供的额外插孔数，范围 [1, 5]
    arr = [random.randint(1, 5) for _ in range(n)]

    result = socket(n, m, k, arr)
    print(result)

if __name__ == "__main__":
    # 示例：指定规模 n
    main(10)