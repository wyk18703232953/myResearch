import random

def ch_x(stri, n):
    res = ''
    for i in range(len(stri)):
        if i != n:
            res += stri[i]
        else:
            res += 'x'
    return res

def main(n):
    # 根据规模 n 生成测试数据
    # 这里生成两个长度为 n 的随机01串
    a = ''.join(random.choice('01') for _ in range(n))
    b = ''.join(random.choice('01') for _ in range(n))

    cnt = 0
    a_cur = a
    b_cur = b

    for i in range(len(a_cur)):
        if a_cur[i] == '0' and b_cur[i] == '0':
            c = [i - 1, i + 1]
            for e in c:
                if 0 <= e < len(a_cur):
                    if a_cur[e] == '0':
                        cnt += 1
                        a_cur = ch_x(a_cur, e)
                        break
                    if b_cur[e] == '0':
                        cnt += 1
                        b_cur = ch_x(b_cur, e)
                        break
            a_cur = ch_x(a_cur, i)
            b_cur = ch_x(b_cur, i)

    print(cnt)
    return cnt

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)