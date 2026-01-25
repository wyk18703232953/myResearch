import string

def main(n):
    if n <= 0:
        print(-1)
        return

    # 构造确定性的 s1 和 s2，长度均为 n
    lower = string.ascii_lowercase
    m = len(lower)

    # s1: 周期性从 a-z 取字符
    s1 = [lower[i % m] for i in range(n)]

    # s2: 对 s1 做一个确定性的循环右移和局部翻转，保持字符频次相同
    shift = n // 3
    s2 = [s1[(i - shift) % n] for i in range(n)]
    # 在前 n//2 段再做一次确定性翻转
    half = n // 2
    s2[:half] = reversed(s2[:half])

    # 以下为原核心算法逻辑（去掉所有输入相关）
    s1 = list(s1)
    s2 = list(s2)
    count = 0
    ans = []
    lower = string.ascii_lowercase
    np_flag = 0
    for ch in lower:
        if s1.count(ch) != s2.count(ch):
            np_flag += 1
            break
    if np_flag > 0:
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
            pos = dict()
            for j in range(n):
                if s1[j] in pos:
                    pos[s1[j]].append(j)
                else:
                    pos[s1[j]] = [j]

    print(len(ans))
    if ans:
        print(*ans)
    else:
        print()

if __name__ == "__main__":
    main(10)