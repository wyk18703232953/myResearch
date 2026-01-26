import math

def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)

def generate_inputs(n):
    # 第一行：长度为 n，由 '+', '-' 构成
    s1 = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    # 第二行：长度为 n，由 '+', '-', '?' 构成
    pattern = ['+', '-', '?']
    s2 = ''.join(pattern[i % 3] for i in range(n))
    return s1, s2

def core_logic(s1, s2):
    dict1 = {'+': 0, '-': 0, '?': 0}
    for i in s1:
        dict1[i] += 1
    for i in s2:
        if i == '?':
            dict1[i] += 1
        else:
            dict1[i] -= 1

    if dict1['+'] < 0 or dict1['-'] < 0:
        return 0.000000000000
    elif dict1['+'] == 0 and dict1['-'] == 0:
        return 1.000000000000
    elif dict1['+'] and dict1['-']:
        ans = (nCr(dict1['?'], dict1['+']) / (2 ** dict1['?']))
        return ans
    else:
        ans = (1 / (2 ** dict1['?']))
        return ans

def main(n):
    s1, s2 = generate_inputs(n)
    ans = core_logic(s1, s2)
    # 输出格式与原程序保持一致
    print("%.12f" % ans)

if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值进行规模实验
    main(10)