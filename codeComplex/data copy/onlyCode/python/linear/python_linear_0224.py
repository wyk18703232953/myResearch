n=int(input())
s=input()
if "0" in s:
    if "1" in s:
        print("1"+"0"*s.count("0"))
    else:
        print("0")
else:
    print("1")