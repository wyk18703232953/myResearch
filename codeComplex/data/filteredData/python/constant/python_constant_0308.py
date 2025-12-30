import random

def main(n):
    # 随机生成测试数据：
    # 约定：k, s, p 的规模与 n 同级，以保证有意义的测试
    # k: 1 ~ n
    # s: 1 ~ n
    # p: 1 ~ n
    k = random.randint(1, max(1, n))
    s = random.randint(1, max(1, n))
    p = random.randint(1, max(1, n))

    # 保持原程序中 n 的含义，这里的 n 为规模参数，复用为题目中的 n
    # 若想区分可用其他变量名，这里按要求保留 main(n) 接口
    paper_person = (n + s - 1) // s
    total_needed = paper_person * k
    ans = (total_needed + p - 1) // p

    print(ans)


if __name__ == "__main__":
    # 示例：使用 n=10 运行一次
    main(10)