for _ in range(int(input())):
    s = input()
    ro=co=0
    for c in s:
        if '0'<= c <= '9': ro = 10*ro+int(c)
        elif ro:
            ro, co = s[1:].split('C'); co=int(co)
            v = ''
            while co:
                co-=1
                r = co%26
                co = co//26
                v += chr(65+r)
            print(v[::-1]+ro)
            break
        else: co = co*26 + ord(c) - 64
    else:
        print("R{}C{}".format(ro, co))
    
