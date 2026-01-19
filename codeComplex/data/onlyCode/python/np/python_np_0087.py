from math import factorial,pow
s1=list(input())
s2=list(input())
S1={"+":0, "-":0}
S2={"+":0, "-":0, "?":0}
for i in s1:
    S1[i]+=1
for i in s2:
    S2[i]+=1
if S1["+"]-S2["+"]>=0 and S1["-"]-S2["-"]>=0:
    pos=S1["+"]-S2["+"]
    neg=S1["-"]-S2["-"]
    ques=S2["?"]
    res=(factorial(pos+neg)/(factorial(pos)*factorial(neg)))/pow(2,ques)
    print("%.12f"%res)
else:
    print("%.12f" % 0)