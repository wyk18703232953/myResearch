from string import digits
from collections import Counter

def main(n):
    # 构造确定性输入 a 和 b，长度和内容由 n 决定
    # a 的长度为 n，b 的长度为 n（若 n 为 0，则为 1，以保持行为）
    if n <= 0:
        a_len = 1
        b_len = 1

    else:
        a_len = n
        b_len = n

    # a: 依次循环使用 digits 中的字符
    a = "".join(digits[i % 10] for i in range(a_len))
    # b: 使用 digits 的反向顺序生成
    rd = digits[::-1]
    b = "".join(rd[i % 10] for i in range(b_len))

    ca = Counter(a)
    l = list()
    if len(b) > len(a):
        for i in digits[::-1]:
            if i in ca:
                l.extend(i * ca[i])

    else:
        def asd(i, s):
            if i == len(b):
                return True
            if s:
                for j in digits[::-1]:
                    if j in ca and ca[j] > 0:
                        l.extend(j * ca[j])
                return True

            else:
                for j in digits[:int(b[i])+1][::-1]:
                    if j in ca and ca[j] > 0:
                        ca[j] -= 1
                        l.append(j)
                        if asd(i + 1, j != b[i]):
                            return True
                        ca[j] += 1
                        l.pop()
                return False
        asd(0, False)
    # print("".join(l))
    pass
if __name__ == "__main__":
    main(10)