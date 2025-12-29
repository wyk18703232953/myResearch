# time - O(n)
# space - O(1)

import random

def substring(x, s):
    count = 0
    ans = 0

    for i in range(x):
        if s[i] == "x":
            count += 1
        else:
            if count >= 3:
                ans += count - 2
            count = 0
    if count >= 3:
        ans += count - 2

    return ans

def main(n):
    # 3/4 概率为 'x'，1/4 概率为非 'x'，以便较多测试到连续 'x'
    chars = ['x', 'a']
    weights = [0.75, 0.25]
    s_list = random.choices(chars, weights=weights, k=n)
    s = ''.join(s_list)
    x = n

    result = substring(x, s)
    print(result)

if __name__ == "__main__":
    # 示例：用 n = 20 运行
    main(20)