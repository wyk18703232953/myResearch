import random
import string

def main(n: int):
    # 生成长度为 n 的测试字符串（小写字母）
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    ans = 0
    amap = {}

    # 逻辑与原程序 fun() 一致
    for strLen in range(n, 0, -1):
        mark = 0
        for t in range(0, n):
            if t + strLen > n:
                break
            sub = s[t:t + strLen]
            if sub in amap:
                amap[sub] += 1
            else:
                amap[sub] = 1
            if amap[sub] >= 2:
                mark = 1
                ans = len(sub)
                print(ans)
                break
        if mark == 1:
            break

    if ans == 0:
        print(ans)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)