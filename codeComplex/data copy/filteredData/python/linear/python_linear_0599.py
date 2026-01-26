n_global = None

def main(n):
    global n_global
    n_global = n
    c = 0
    for j in range(2, 1 + n // 2):
        e = 0
        i = n // j
        e += (i * (i + 1)) // 2
        e -= 1
        if e > 0:
            c += e
    result = c * 4
    return result

if __name__ == "__main__":
    # 示例调用：可以按需修改 n 的值进行时间复杂度实验
    test_n = 1000
    # print(main(test_n))
    pass