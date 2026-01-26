a = input()
b = input()
digits = {}
def greedy(digits,s):
    for i in range(9,-1,-1):
        d = str(i)
        if d in digits:
            while digits[d] > 0:
                s += d
                digits[d] -= 1
    return s
for d in a:
    if d in digits:
        digits[d] += 1
    else:
        digits[d] = 1
if len(a) < len(b):
    print(greedy(digits,""))
else:
    ind = 0
    cur = ""
    back = False
    done = False
    while 1:
        if ind == len(a) or done == True:
            break
        found = False
        for i in range(9,-1,-1):
            x = str(i)
            if i == int(b[ind]) and x in digits and digits[x] > 0:
                found = True
                digits[x] -= 1
                cur += x
                break
            elif i < int(b[ind]) and x in digits and digits[x] > 0:
                found = True
                done = True
                digits[x] -= 1
                cur += x
                print(greedy(digits,cur))
                break
        if found == False:
            back = True
            break
        ind += 1
    
    if back == False and done == False:
        print(cur)
    elif done == False:
        for i in range(ind-1,-1,-1):
            digits[cur[i]] += 1
            for j in range(9,-1,-1):
                d = str(j)
                if j < int(b[i]) and d in digits and digits[d] > 0:
                    done = True
                    s = cur[:i]
                    s += d
                    digits[d] -= 1
                    print(greedy(digits,s))
                    break
            if done:
                break