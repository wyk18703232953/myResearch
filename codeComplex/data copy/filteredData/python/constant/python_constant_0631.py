import math,string,itertools,fractions,heapq,collections,re,array,bisect,copy,functools

inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def main(n):
    q = n
    rr = []

    def f(a,b,c,d):
        if a > c or b > d:
            return (0,0)
        sa = c-a + 1
        sb = d-b + 1
        g = h = (sa * sb) // 2
        if (sa*sb) % 2 == 1:
            g += 1
        if (a+b) % 2 == 0:
            return (g,h)
        return (h,g)

    def fa(a):
        return f(a[0],a[1],a[2],a[3])

    for i in range(q):
        n_i = 2 + (i % 50)
        m_i = 2 + (i % 50)
        n2 = n_i // 2
        m2 = m_i // 2
        wa = [1, 1, n2, m2]
        ba = [n2+1, m2+1, n_i, m_i]

        wc,bc = f(1,1,n_i,m_i)
        w1,b1 = fa(wa)
        w2,b2 = fa(ba)
        w3,b3 = f(max(wa[0],ba[0]),max(wa[1],ba[1]),min(wa[2],ba[2]),min(wa[3],ba[3]))

        wc += b1
        bc -= b1
        wc -= w2
        bc += w2
        wc -= b3
        bc += b3
        rr.append('{} {}'.format(wc,bc))

    return "\n".join(map(str,rr))

if __name__ == "__main__":
    # print(main(10))
    pass