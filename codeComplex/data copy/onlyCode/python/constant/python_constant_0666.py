
a0 = (1 << 30) - 1

a0 = 3
b0 = 1

def mock_query(c, d):
    res = (a0 ^ c) - (b0 ^ d)
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0

def query2(c, d):
    ans = mock_query(c, d)
    print('? {:08b} {:08b} --> {}'.format(c, d, ans))
    return ans

def query(c, d):
    print('?', c, d)
    return int(input())

# query = query2

def solve():
    a = 0
    b = 0
    last_ans = query(0, 0)

    pos = 29
    while pos >= 0:
        bit = 1 << pos

        ans = query(a + bit, b + bit)
        if (last_ans, ans) == (1, -1):
            a += bit
            last_ans = query(a, b)
        elif (last_ans, ans) == (-1, 1):
            b += bit
            last_ans = query(a, b)
        # elif ans == 0:
            # pass
        else:
            last_ans = ans
            ans = query(a + bit, b)
            if ans == -1:
                a += bit
                b += bit

        pos -= 1

    print('!', a, b)

solve()
