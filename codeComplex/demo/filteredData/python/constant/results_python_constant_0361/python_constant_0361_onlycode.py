dict={"Power":"purple",
      "Time":"green",
      "Space":"blue",
      "Soul":"orange",
      "Reality":"red",
      "Mind":"yellow"}
dict1={}
n=(int(input()))
while n:
    str=input()
    if str=="purple":
        dict1["Power"]=str
    elif str=="green":
        dict1["Time"]=str
    elif str=="blue":
        dict1["Space"]=str
    elif str=="orange":
        dict1["Soul"]=str
    elif str=="red":
        dict1["Reality"]=str
    elif str=="yellow":
        dict1["Mind"]=str
    n-=1

val=list(dict.keys())
val_list=list(dict1.keys())
l=[key for key in val if key not in val_list]
print(len(l))
for i in range(len(l)):
    print(l[i])