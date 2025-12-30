import random

def main(n):
    # 1. 生成长度为 n 的随机数字串（每位是 0~9）
    s = ''.join(str(random.randint(0, 9)) for _ in range(n))

    # 2. 原逻辑封装
    ans = 0
    r, c = 0, 0
    for ch in s:
        r += int(ch)
        c += 1
        if int(ch) % 3 == 0 or r % 3 == 0 or c == 3:
            ans += 1
            r, c = 0, 0

    # 输出结果（也可改为 return ans, s 供调试）
    print(ans)

if __name__ == "__main__":
    # 示例调用：n 可根据需要修改
    main(10)