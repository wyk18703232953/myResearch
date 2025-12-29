import string
import random

def main(n):
    # 随机选择 k（1 到 26 且不超过 n）
    k = random.randint(1, min(26, n if n > 0 else 1))

    # 构造字母表前 k 个大写字母
    letters = string.ascii_uppercase[:k]

    # 生成长度为 n 的测试字符串，字符从 letters 中随机选
    s = ''.join(random.choice(letters) for _ in range(n))

    # 原逻辑
    mp = {ch: 0 for ch in letters}
    for ch in s:
        if ch in mp:
            mp[ch] += 1
    result = min(mp.values()) * k

    # 输出结果（可根据需要决定是否也返回）
    print(result)
    return result

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(100)