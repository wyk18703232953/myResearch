import random
import string

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 1) a：字符串 c 中不同字母的最大数量（1 到 min(26, n)）
    # 2) b：要选择的字母数量（1 到 a）
    # 3) c：长度为 n 的小写字母串
    max_distinct = min(26, max(1, n))  # 至多 26 个不同字母
    a = random.randint(1, max_distinct)

    # 构造一个有 a 个不同字母的字符串 c，长度为 n
    letters = random.sample(string.ascii_lowercase, a)
    c_chars = []
    for _ in range(n):
        c_chars.append(random.choice(letters))
    c = "".join(c_chars)

    # b 在 1..a 之间
    b = random.randint(1, a)

    # 以下为原逻辑（去掉 input）：
    summa = 0
    count = 0
    j = -2
    i = 0
    abc = "abcdefghijklmnopqrstuvwxyz"
    # 按字母表从前往后选满足间隔条件的字母
    while i < 26 and count < b:
        if abc[i] in c and i - 2 >= j:
            summa += i + 1
            count += 1
            j = i
        i += 1

    if count < b:
        print(-1)
    else:
        print(summa)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)