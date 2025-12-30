def main(n):
    # 1. 生成测试数据：
    #    - n: 项目个数
    #    - k: 总时间限制（这里随 n 简单设定为 3*n，可按需调整）
    #    - 对于每个项目 i：
    #        a: 该项目可参与的最小人数（1 到 n）
    #        t: 完成该项目所需时间（1 到 10）
    #
    #    注意：原逻辑要求所有 n 个项目读入，规模即为 n。
    import random

    random.seed(0)
    k = 3 * n

    b = []
    for i in range(n):
        a = random.randint(1, n)
        t = random.randint(1, 10)
        b.append([a, t, i + 1])  # [最小人数 a, 时间 t, 原始编号 i+1]

    # 2. 按原始程序逻辑处理（去掉所有 input / I/O 包装）

    b.sort(key=lambda x: x[1])  # 按时间 t 升序

    ans = 0
    j = 0
    curr = 1           # 当前尝试的组人数
    currsum = 0        # 当前人数下，在可参加的项目中选到的时间总和
    d = dict()         # d[r] = 对人数 r 有效的项目时间之和（在遍历中使用）
    e = dict()         # e[r] = 对人数 r 有效的项目个数
    l = 0              # 当前已经选了多少个项目（对 curr 人数）

    while curr <= n:
        # 移除对于 curr-1 人数时的项目贡献
        if curr - 1 in d:
            currsum -= d[curr - 1]
            l -= e[curr - 1]

        # 在排序后的项目中继续往前试着加入项目
        while j < n:
            if b[j][0] >= curr:
                currsum += b[j][1]
                if b[j][0] in d:
                    d[b[j][0]] += b[j][1]
                    e[b[j][0]] += 1
                else:
                    d[b[j][0]] = b[j][1]
                    e[b[j][0]] = 1
                l += 1
            if l == curr:  # 已经有 curr 个可参加项目
                j += 1
                break
            j += 1

        # 判断这一人数 curr 是否可行
        if j <= n and l == curr and currsum <= k:
            ans += 1
        else:
            break
        curr += 1

    # 根据求得的 ans（最大可行人数），输出项目编号列表
    c = []
    j = 0
    l = 0
    while j < n:
        if l == ans:
            break
        if b[j][0] >= ans:
            c.append(b[j][2])
            l += 1
        j += 1

    # 原程序输出：
    # print(ans)
    # print(ans)
    # print(*c)
    #
    # 保持原有输出格式，改为 return 字典，方便外部调用或测试。
    return {
        "ans": ans,
        "ans_again": ans,
        "chosen_indices": c,
        "k": k,
        "data": b,  # 包含生成的测试数据（a, t, index）
    }


# 示例：在本文件直接运行时简单测试
if __name__ == "__main__":
    result = main(10)
    print(result["ans"])
    print(result["ans_again"])
    print(*result["chosen_indices"])