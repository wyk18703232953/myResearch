import random

def main(n):
    # 根据 n 生成测试数据：
    # 原程序中有 n, m 两个输入，这里 m 未使用，仅构造一个与 n 同规模量级的 m 用于模拟
    m = random.randint(1, max(1, 2 * n))

    # 原逻辑开始
    c = 0
    ans = ""
    for _ in range(n):
        ans += str(c ^ 1)
        c = c ^ 1
    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)