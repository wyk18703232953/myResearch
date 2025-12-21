def main(n):
    k = n
    sol = ''
    cnt = 0
    for i in range(1, 13):
        inc = 9 * (10 ** (i - 1)) * i
        if cnt + inc >= k:
            break
        else:
            cnt += inc
    lft = k - cnt
    dig = (lft) / i
    if dig != int(dig):
        dig = int(dig + 1)
    else:
        dig = int(dig)
    num = (10 ** (i - 1)) + dig - 1
    left = k - (cnt + dig * i)
    sol = str(num)
    return sol[left - 1]


if __name__ == "__main__":
    print(main(100))