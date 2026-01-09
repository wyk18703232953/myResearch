op=[0]*1000000
cl=[0]*1000000

def fun(s):
    v = []
    for i in range(len(s)):
        l = len(v)
        if s[i]=='(':
            v.append(s[i])
        elif l>0 and v[l-1]=='(':
            v.pop()

        else:
            v.append(')')
    l = len(v)
    if l==0:
        op[0]+=1
        cl[0]+=1
    elif v[0]==v[l-1]:
        if v[0]=='(':
            op[l]+=1

        else:
            cl[l]+=1

def main(n):
    global op, cl
    op = [0]*1000000
    cl = [0]*1000000

    # 解释：n 作为测试用例数量，每个字符串长度也与 n 挂钩，保证可规模化
    t = n
    for case_id in range(t):
        # 生成一个确定性的括号串
        # 长度随 n 和 case_id 变化，但不会太大以避免越界
        length = (case_id + 1) * (n % 10 + 1)
        # 交替生成 '(' 和 ')'，并根据 case_id 决定起始字符，保证多样性但确定性
        s = ''.join('(' if (i + case_id) % 2 == 0 else ')' for i in range(length))
        fun(s)

    ans = 0
    for i in range(1000000):
        ans += op[i] * cl[i]
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)