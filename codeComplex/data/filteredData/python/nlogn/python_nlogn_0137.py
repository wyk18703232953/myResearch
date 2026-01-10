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
    # 规模含义：
    # n: 数组长度，同时用来构造 m, k 的规模
    if n <= 0:
        return

    # 确定性构造参数
    m = n * 2 + 3          # 需要连接的设备数
    k = max(1, n // 3)     # 初始插座数

    # 确定性构造 arr：长度为 n 的正整数列表
    # 使用简单算术构造，避免非确定性
    arr = [(i % 5) + 1 for i in range(1, n + 1)]

    res = socket(n, m, k, arr)
    print(res)


if __name__ == "__main__":
    # 示例：可以修改这里的 n 来做不同规模的实验
    main(10)