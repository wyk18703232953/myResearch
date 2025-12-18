a1, a2, b1, b2, c1, c2 = map(int, input().split())
l = max([a1, a2, b1, b2, c1, c2])

if (a1*a2 + b1*b2 + c1*c2 != l**2):
    print(-1)
else:
    if a1 > a2:
        a1, a2 = a2, a1
    if b1 > b2:
        b1, b2 = b2, b1
    if c1 > c2:
        c1, c2 = c2, c1
    
    if a2 == b2 and b2 == c2:
        print(l)
        for i in range(a1):
            print('A'*a2)
        for i in range(b1):
            print('B'*b2)
        for i in range(c1):
            print('C'*c2)
    else:
        ls = [[a1, a2, 'A'], [b1, b2, 'B'], [c1, c2, 'C']]
        
        if b2 == l:
            ls[0], ls[1] = ls[1], ls[0]
        if c2 == l:
            ls[0], ls[2] = ls[2], ls[0]

        valid = True
        if ls[1][0] == ls[2][0]:
            pass
        elif ls[1][1] == ls[2][1]:
            ls[1][0], ls[1][1] = ls[1][1], ls[1][0]
            ls[2][0], ls[2][1] = ls[2][1], ls[2][0]
        elif ls[1][0] == ls[2][1]:
            ls[2][0], ls[2][1] = ls[2][1], ls[2][0]
        elif ls[1][1] == ls[2][0]:
            ls[1][0], ls[1][1] = ls[1][1], ls[1][0]
        else:
            valid = False

        if (ls[1][0] + ls[0][0] != l) or (ls[1][1] + ls[2][1] != l):
            valid = False

        if not valid:
            print(-1)
        else:
            print(l)

            for i in range(ls[0][0]):
                print(ls[0][2] * l)
            for i in range(ls[1][0]):
                print(ls[1][2] * ls[1][1] + ls[2][2] * ls[2][1])
