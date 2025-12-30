import random
import string

def main(n):
    # 生成长度为 n 的随机小写字符串 s
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
    # 打乱 s 得到 t（保证为同一多重集合）
    t_list = list(s)
    random.shuffle(t_list)
    t = ''.join(t_list)

    # 以下为原算法逻辑（去掉输入）
    if sorted(s) != sorted(t):
        print(-1)
        return

    s = list(s)
    t = list(t)
    ans = []
    for i in range(n):
        for j in range(i, n - 1):
            if s[j + 1] == t[i]:
                # 把 s[j+1] 向左冒泡到位置 i
                for k in range(j, i - 1, -1):
                    ans.append(k + 1)
                    s[k + 1], s[k] = s[k], s[k + 1]
                break

    print(len(ans))
    if ans:
        print(*ans)


if __name__ == "__main__":
    # 示例：规模设为 10，可按需要修改
    main(10)