from math import factorial

s1 = input()
s2 = input()

cnt_plus_1, cnt_plus_2 = 0, 0
cnt_minus_1, cnt_minus_2 = 0, 0
cnt_question = 0

for i in range(len(s1)):
    if s1[i] == "+": cnt_plus_1 += 1
    if s1[i] == "-": cnt_minus_1 += 1

    if s2[i] == "+": cnt_plus_2 += 1
    if s2[i] == "-": cnt_minus_2 += 1

    if s2[i] == "?": cnt_question += 1

if cnt_question == 0:
    if cnt_plus_1 == cnt_plus_2:
        print("{:.9f}".format(1.0))
    else:
        print("{:.9f}".format(0.0))
elif cnt_plus_2 + cnt_question < cnt_plus_1 or cnt_plus_2 > cnt_plus_1:
    print("{:.9f}".format(0.0))
else:
    dP = cnt_plus_1 - cnt_plus_2
    dM = cnt_question - dP

    if dM == 0 or dP == 0:
        print("{:0.9f}".format(1 / (2**cnt_question)))
    else:
        CP = factorial(cnt_question) / (factorial(dP)*factorial(cnt_question - dP))
        print((CP * (0.5 ** dP) * (1 - 0.5) ** (cnt_question - dP)))
