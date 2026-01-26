def main(n):
    # 1. 预生成所有不超过 2e9 的 2 的幂
    ak = []
    i = 0
    while 2 ** i <= 2000000000:
        ak.append(2 ** i)
        i += 1

    # 2. 生成规模为 n 的测试数据 a
    # 这里简单生成 1..n 的序列，你可以按需要修改生成逻辑
    a = list(range(1, n + 1))

    # 3. 原逻辑：统计有多少元素不能与其它元素配对成 2 的幂
    pos_dict = dict()
    for idx, v in enumerate(a):
        if v not in pos_dict:
            pos_dict[v] = set()
        pos_dict[v].add(idx)

    ans = [0] * n
    for i in range(n):
        for j in ak:
            need = j - a[i]
            if need in pos_dict:
                if (need == a[i] and len(pos_dict[a[i]]) >= 2) or need != a[i]:
                    ans[i] = 1
                    break

    # 返回结果而不是打印，方便在外部调用和测试
    return ans.count(0)


if __name__ == "__main__":
    # 示例：调用 main(10)
    result = main(10)
    # print(result)
    pass