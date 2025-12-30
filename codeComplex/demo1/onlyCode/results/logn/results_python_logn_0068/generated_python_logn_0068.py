from math import *

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里生成两个整数 l, r，满足 0 <= l <= r < 2^n
    # 你可以按需修改生成策略
    l = (1 << (n - 1)) - 1  # 例如：011...1 (n-1 个 1)
    r = (1 << n) - 1        # 例如：111...1 (n 个 1)

    # 原逻辑开始
    l_bin = list(bin(l)[2:])
    r_bin = list(bin(r)[2:])
    # 在前面补 0，使得 l_bin 与 r_bin 等长
    l_bin = ['0' for _ in range(len(r_bin) - len(l_bin))] + l_bin

    s = ""
    for i in range(len(r_bin)):
        if l_bin[i] == r_bin[i]:
            s += "0"
        else:
            s += "1" * (len(r_bin) - i)
            break

    ans = int(s, 2)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改或由外部调用 main(n)
    main(5)