import random

def main(n: int):
    # 根据规模 n 生成测试数据 s, t
    # 约束：保证 len(s) == len(t)，且 s 中只包含 '0'-'9'
    # 为了让逻辑有意义，这里生成：
    #   s: 长度为 n 的随机数字串
    #   t: 长度为 n 的随机数字串
    # 如需其他生成方式，可自行修改。
    s = [str(random.randint(0, 9)) for _ in range(n)]
    t = [str(random.randint(0, 9)) for _ in range(n)]

    # 原逻辑的复制与调整（不使用 input()）
    if len(s) < len(t):
        s.sort(reverse=True)
        print(''.join(s))
    else:
        count = [0] * 10
        for elm in s:
            count[ord(elm) - ord('0')] += 1
        ans = []
        less = False
        for i in range(len(s)):
            for j in range(9, -1, -1):
                if not less:
                    if j <= ord(t[i]) - ord('0') and count[j] > 0:
                        if j < ord(t[i]) - ord('0'):
                            ans.append(chr(j + ord('0')))
                            count[j] -= 1
                            less = True
                            break
                        else:
                            curr_num = 0
                            for k in range(10):
                                if j == k:
                                    for _ in range(count[k] - 1):
                                        curr_num = curr_num * 10 + k
                                else:
                                    for _ in range(count[k]):
                                        curr_num = curr_num * 10 + k
                            rest_num = 0
                            for k in range(i + 1, len(s)):
                                rest_num = rest_num * 10 + (ord(t[k]) - ord('0'))
                            if rest_num >= curr_num:
                                ans.append(chr(j + ord('0')))
                                count[j] -= 1
                                break
                            else:
                                continue
                else:
                    if count[j] > 0:
                        ans.append(chr(j + ord('0')))
                        count[j] -= 1
                        break
        print(''.join(ans))


if __name__ == '__main__':
    # 示例：运行规模为 5 的测试
    main(5)