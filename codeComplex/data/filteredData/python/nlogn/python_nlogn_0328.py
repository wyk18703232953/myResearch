def main(n):
    # 生成测试数据：n 个字符串
    # 这里示例生成：长度从 1 到 n（不超过 100），每个长度对应相同的字符串 'a' * length
    # 可根据需要自定义数据生成方式
    strings = []
    max_len = 100
    for i in range(n):
        length = (i % max_len) + 1  # 长度在 1..100 循环
        s = 'a' * length           # 同长度使用相同字符串，保证答案为 YES
        strings.append(s)

    # 以下是将原逻辑封装，不使用 input()
    string = [[] for _ in range(100)]
    for val in strings:
        size = len(val)
        if size > 100:
            # 原代码只开了 100 个桶，如果长度超过 100 就无法放入
            # 为保持原语义，直接判定为 NO
            print("NO")
            return
        string[size - 1].append(val)

    for i in range(100):
        if len(string[i]) > 0:
            string[i].sort()

    ans = []
    poss = True

    # 检查每个长度桶中是否所有字符串相同
    for i in range(100):
        if len(string[i]) == 0:
            continue
        row = string[i]
        if len(set(row)) > 1:
            poss = False

    if not poss:
        print("NO")
        return

    # 检查按长度递增时，前一个长度组的代表串是否是后一个长度组代表串的子串
    for i in range(100):
        if len(string[i]) == 0:
            continue
        for j in range(i + 1, 100):
            if len(string[j]) == 0:
                continue
            sub_string = string[i][0]
            main_str = string[j][0]
            if sub_string in main_str:
                # 找到一个后续长度组满足条件，就跳到下一长度 i
                break
            else:
                poss = False
                break
        if not poss:
            break

    if not poss:
        print("NO")
    else:
        print("YES")
        for i in range(100):
            if len(string[i]) == 0:
                continue
            for j in range(len(string[i])):
                print(string[i][j])


if __name__ == "__main__":
    # 示例运行：n=5
    main(5)