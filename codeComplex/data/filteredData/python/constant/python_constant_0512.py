import random

def main(n):
    # 生成 n 组测试数据并执行原逻辑
    for _ in range(n):
        # 按规模 n 生成数据：a, b, d 在 [0, 2*n] 范围内
        d = random.randint(0, 2 * n)
        a = random.randint(0, d)  # 保证有一定概率 a,b <= d
        b = random.randint(0, d)

        if a > d or b > d:
            print(-1)
        elif a % 2 == b % 2:
            if a % 2 == d % 2:
                print(d)
            else:
                print(d - 2)
        else:
            # 下面这个分支在原代码中是多余的嵌套，但保持逻辑完全一致
            if a % 2 == b % 2:
                if d % 2 == a % 2:
                    print(d)
                else:
                    print(d - 2)
            else:
                print(d - 1)


if __name__ == "__main__":
    # 示例：运行规模为 5
    main(5)