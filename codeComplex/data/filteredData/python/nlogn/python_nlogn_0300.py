import random

def main(n):
    # 1. 生成测试数据
    # 生成 n 个权重 w：范围 [1, 10^9]
    w = [random.randint(1, 10**9) for _ in range(n)]
    # 生成长度为 2n 的指令串 s，包含 n 个 '0' 和 n 个 '1'
    s_list = ["0"] * n + ["1"] * n
    random.shuffle(s_list)
    s = "".join(s_list)

    # 2. 原始逻辑
    intro = [[v, i] for i, v in enumerate(w, 1)]
    intro.sort(key=lambda x: x[0])
    i = -1
    li = []
    ans = []
    for j in s:
        if j == "0":
            i += 1
            ans.append(intro[i][1])
            li.append(intro[i][1])
        else:
            ans.append(li.pop(-1))
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    # 示例：可根据需要调整规模 n
    main(5)