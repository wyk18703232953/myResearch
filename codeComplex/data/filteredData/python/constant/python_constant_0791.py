import math
import random

def main(n):
    # 生成规模为 n 的测试数据：T 个测试用例及对应的 N 值
    T = n
    test_cases = []

    # 一部分构造为必然 YES 的数据，剩余随机
    for i in range(T):
        choice = i % 4
        if choice == 0:
            # 形如 2 * (k^2) 的数 -> YES
            k = random.randint(1, max(1, n))
            N = 2 * (k * k)
        elif choice == 1:
            # 形如 4 * (k^2) 的数 -> YES
            k = random.randint(1, max(1, n))
            N = 4 * (k * k)
        elif choice == 2:
            # 生成一个奇数 -> NO
            N = random.randint(1, 2 * n - 1)
            if N % 2 == 0:
                N += 1
        else:
            # 完全随机的正整数
            N = random.randint(1, 4 * n * n + 10)
        test_cases.append(N)

    # 根据原逻辑处理并输出结果
    print(T)
    for N in test_cases:
        print(N)
        if N % 2 == 1:
            print("NO")
        else:
            N_half = N // 2
            root = int(math.isqrt(N_half))
            if root * root == N_half:
                print("YES")
            else:
                if N_half % 2 == 1:
                    print("NO")
                else:
                    N_quarter = N_half // 2
                    root2 = int(math.isqrt(N_quarter))
                    if root2 * root2 == N_quarter:
                        print("YES")
                    else:
                        print("NO")


if __name__ == "__main__":
    # 示例：可修改 n 来控制测试规模
    main(5)