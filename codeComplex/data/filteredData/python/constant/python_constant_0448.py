import random

def main(n: int):
    # 根据 n 生成 m（这里示例为 1 到 n 的随机数，可按需调整生成规则）
    m = random.randint(1, max(1, n))

    # 保留原程序的核心逻辑（与 n、m 无关，只是演示如何封装）
    ans1 = "1" * 1500
    ans2 = "8" * 1499 + "9"

    print(ans1)
    print(ans2)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需调整
    main(10)