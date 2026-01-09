def main(n):
    # 生成确定性的字符串，长度为 n
    # 使用循环的 'abc' 模式，确保存在重复子串以保持算法行为
    base = ['a', 'b', 'c']
    name_chars = [base[i % 3] for i in range(n)]
    name = ''.join(name_chars)

    for i in range(len(name), 0, -1):
        for j in range(len(name) - i + 1):
            if name[j: j + i] in name[j + 1:]:
                # print(i)
                pass
                return
    # print(0)
    pass
if __name__ == "__main__":
    main(10)