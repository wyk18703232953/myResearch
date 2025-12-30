def main(n):
    # 根据 n 生成测试数据：
    # 构造一个长度为 n 的字符串 s 和其打乱后的 d，
    # 这样 sorted(s) == sorted(d) 恒成立，便于检验逻辑。
    import random
    random.seed(0)

    # 生成一个基础字符列表，循环使用 'a'..'z'
    base_chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = base_chars[:]          # 原始序列
    d = base_chars[:]
    random.shuffle(d)          # 目标序列

    # 保持与原始逻辑一致：s、d 为列表
    if sorted(s) != sorted(d):
        print(-1)
        return

    ans = []
    for i in range(n):
        if s[i] != d[i]:
            # 在后面寻找第一个等于 d[i] 的位置 ind
            ind = None
            for u in range(i + 1, n):
                if s[u] == d[i]:
                    ind = u
                    break
            if ind is None:
                # 理论上不应发生，因为 sorted(s) == sorted(d)
                print(-1)
                return

            cnt = abs(ind - i)
            # 将 s[ind] 删除并插入到位置 i
            s.pop(ind)
            s.insert(i, d[i])

            # 记录操作序列
            for _ in range(cnt):
                if ind > 0:
                    ans.append(ind)
                else:
                    ans.append(1)
                ind -= 1

    print(len(ans))
    if ans:
        print(*ans)


if __name__ == "__main__":
    # 示例调用，可自行修改 n 测试不同规模
    main(5)