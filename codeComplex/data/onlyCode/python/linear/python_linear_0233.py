#"xxx"が連続部分文字列としていくつ含まれるか
#文字ごとでグループに分ければキーがxのグループのみに注目することができる
#xがキーのグループの長さをlとするならmax(0,l-3+1)がそのグループに含まれる"xxx"の個数
from itertools import groupby
n=int(input())
s=input()
x=[len(list(group)) for key,group in groupby(s) if key=="x"]
ans=sum(max(0,l-3+1) for l in x)
print(ans)