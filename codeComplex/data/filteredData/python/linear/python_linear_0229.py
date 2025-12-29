import random
import string

def main(n: int):
    # 生成长度为 n 的随机字符串，只包含 'x' 和其他字母
    # 为了更接近原题场景，这里用 'x' 和 'o'
    chars = ['x', 'o']
    s = ''.join(random.choice(chars) for _ in range(n))

    count = 0
    temp_count = 0
    for c in s:
        if c == 'x':
            temp_count += 1
        else:
            temp_count = 0
        if temp_count == 3:
            count += 1
            temp_count -= 1

    print(count)


if __name__ == "__main__":
    # 示例调用，可根据需要更改 n
    main(10)