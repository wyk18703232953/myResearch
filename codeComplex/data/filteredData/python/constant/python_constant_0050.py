def main(n):
    # 这里假设规模 n 就是要检测的数字本身
    # 如需批量测试，可自行在外层多次调用 main
    s = [4, 7, 44, 77, 47, 74, 444, 777, 477, 447, 744, 474, 747, 774]
    t = 0
    for i in s:
        if n % i == 0:
            print("YES")
            t = 1
            break
    if t == 0:
        print("NO")


if __name__ == "__main__":
    # 示例自动生成测试数据：用一个固定的 n 调用 main
    # 这里选择一个与原题风格类似的数作为测试，例如 47
    test_n = 47
    main(test_n)