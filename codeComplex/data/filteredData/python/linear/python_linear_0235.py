import random

def main(n: int):
    # 根据规模 n 生成长度为 n 的随机仅含 'x' 和 'o' 的字符串
    chars = ['x', 'o']
    s = ''.join(random.choice(chars) for _ in range(n))

    i = 0
    j = 0
    total = 0

    while j < len(s):
        has_x = False
        count = 0
        # 统计从 i 开始连续的 'x' 段
        while j < len(s) and s[i] == 'x' and s[j] == 'x':
            count += 1
            has_x = True
            j += 1

        if count >= 3:
            total += (count - 3) + 1
        if has_x:
            i = j
        else:
            i += 1
            j += 1

    print(total)

if __name__ == "__main__":
    # 示例：规模为 20
    main(20)