import random
import string as strlib

def main(n: int):
    # 1. 生成规模为 n 的随机测试字符串
    # 字符集可按需调整，这里使用小写字母
    s = ''.join(random.choice(strlib.ascii_lowercase) for _ in range(n))

    totalmax = 0
    for x in range(len(s)):
        curr = ""
        suffix = s[x:]
        for y in suffix:
            curr += y
            # 若在后缀 suffix 中 curr 出现至少两次，则更新答案
            if suffix.rfind(curr) != suffix.find(curr):
                totalmax = max(totalmax, len(curr))
                continue

    print(totalmax)


if __name__ == "__main__":
    # 示例：n = 20，可按需修改
    main(20)