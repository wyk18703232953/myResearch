import random
import string

def main(n: int):
    # 生成两个长度为 n 的字符串 s, t，保证排序后相同
    # 做法：先生成随机字符串 s，再对其做一次随机洗牌得到 t
    if n <= 0:
        return

    # 从小写字母中生成字符串
    letters = string.ascii_lowercase
    s_list = [random.choice(letters) for _ in range(n)]
    t_list = s_list[:]  # 拷贝一份
    random.shuffle(t_list)

    s = ''.join(s_list)
    t = ''.join(t_list)

    sl = [c for c in s]
    tl = [c for c in t]
    ans = []

    # 检查是否可以通过交换相邻字符把 s 变成 t
    if ''.join(sorted(s)) != ''.join(sorted(t)):
        print(-1)
        return

    # 模拟原逻辑：把 sl 通过相邻交换变成 tl，记录交换位置
    for i in range(n):
        if sl[i] != tl[i]:
            # 在后面找到需要的字符
            j = i + 1
            while j < n and sl[j] != tl[i]:
                j += 1
            # 将 sl[j] 通过相邻交换移动到位置 i
            for k in range(j - 1, i - 1, -1):
                sl[k], sl[k + 1] = sl[k + 1], sl[k]
                ans.append(k + 1)  # 位置从 1 开始计数

    print(len(ans))
    for pos in ans:
        print(pos, end=' ')
    print()


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)