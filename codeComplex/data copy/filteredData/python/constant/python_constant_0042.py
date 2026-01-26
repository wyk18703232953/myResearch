def check(num):
    l = list(str(num))
    l = list(dict.fromkeys(l))
    if l == ['4', '7'] or l == ['7', '4'] or l == ['4'] or l == ['7']:
        return True

    else:
        return False


def main(n):
    # 这里将 n 作为规模参数直接使用，相当于原程序中从 input() 读入的 n
    lucky = False
    for i in range(3, n + 1):
        if n % i == 0 and check(i):
            lucky = True
            break
    # print("YES" if lucky else "NO")
    pass
if __name__ == "__main__":
    # 生成测试数据：可以根据需要修改 n 的值
    test_n = 100  # 示例规模
    main(test_n)