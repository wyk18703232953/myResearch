import string
import random

def main(n):
    # 生成测试数据：随机打乱的同构字符串
    # 使用前 n 个小写字母或重复使用字母使长度为 n
    base = []
    letters = string.ascii_lowercase
    for i in range(n):
        base.append(letters[i % 26])
    s1 = base[:]                # 原始字符串
    s2 = base[:]                # 目标字符串（打乱）
    random.shuffle(s2)

    # 逻辑开始（由原代码改造）
    s1 = list(s1)
    s2 = list(s2)
    count = 0  # 保留原变量，虽未使用
    ans = []
    lower = string.ascii_lowercase
    np = 0
    for i in lower:
        if s1.count(i) != s2.count(i):
            np += 1
            break
    if np > 0:
        print(-1)
        return

    pos = dict()
    for i in range(n):
        if s1[i] in pos:
            pos[s1[i]].append(i)
        else:
            pos[s1[i]] = [i]

    for i in range(n):
        if s1[i] == s2[i]:
            continue
        else:
            row = pos[s2[i]]
            no = 0
            for j in range(len(row)):
                if row[j] > i:
                    no = row[j]
                    break
            for j in range(no, i, -1):
                ans.append(j)
            s1.pop(no)
            s1.insert(i, s2[i])
            # 重建 pos
            pos = dict()
            for j in range(n):
                if s1[j] in pos:
                    pos[s1[j]].append(j)
                else:
                    pos[s1[j]] = [j]

    print(len(ans))
    if ans:
        print(*ans)

if __name__ == "__main__":
    # 示例调用：可以修改 n 测试不同规模
    main(10)