import re

def main(n):
    # 生成一个只包含 'x' 和 'o' 的字符串，长度为 n
    # 构造中包含一些长连续 'x' 段用于触发算法逻辑
    if n <= 0:
        s = ""

    else:
        # 周期性模式：连续 (i % 5 + 1) 个 'x'，后跟一个 'o'
        # 形成不同长度的 'x' 段
        chars = []
        i = 0
        while len(chars) < n:
            block_len = i % 5 + 1  # 1..5
            for _ in range(block_len):
                if len(chars) < n:
                    chars.append('x')

                else:
                    break
            if len(chars) < n:
                chars.append('o')
            i += 1
        s = ''.join(chars[:n])

    result = sum(len(f) - 2 for f in re.findall('x{3,}', s))
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)