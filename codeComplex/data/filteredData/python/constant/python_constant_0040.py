# -*- coding: utf-8 -*-

def main(n):
    # 这里的 n 作为规模参数，同时也是原程序中的判断上限和被整除的数
    lucky = ["1", "2", "3", "5", "6", "8", "9", "0"]

    ye = False
    for i in range(1, n + 1):
        luck = True
        for char in str(i):
            if char in lucky:
                luck = False
                break

        if luck and n % i == 0:
            print("YES")
            ye = True
            break

    if not ye:
        print("NO")


if __name__ == "__main__":
    # 根据规模 n 生成测试数据：这里将 n 本身作为测试输入
    # 可根据需要修改为其它生成规则
    test_n = 100  # 示例：使用 100 作为规模
    main(test_n)