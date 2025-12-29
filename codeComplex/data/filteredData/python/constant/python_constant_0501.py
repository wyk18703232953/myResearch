import random

def main(n):
    # n 表示要生成的测试组数 q
    q = n
    print(f"q = {q}")

    for _ in range(q):
        # 生成测试数据 (n, m, k)
        # 这里假设规模 n 同时作为生成数据的上界
        nn = random.randint(0, n)
        mm = random.randint(0, n)
        kk = random.randint(0, n)

        print(f"input: {nn} {mm} {kk}", end=" -> output: ")

        if max(nn, mm) > kk:
            print(-1)
        else:
            if (nn + mm) % 2 == 0:
                if max(nn, mm) % 2 != kk % 2:
                    print(kk - 2)
                else:
                    print(kk)
            else:
                print(kk - 1)

if __name__ == "__main__":
    # 举例运行 main，实际使用时由外部调用 main(n)
    main(5)