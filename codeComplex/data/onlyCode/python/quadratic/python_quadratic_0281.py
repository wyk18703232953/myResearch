n,m=(int(x) for x in input().split())
sequence=input().split()[:n]
fingerprint=input().split()[:m]
print(" ".join(i for i in sequence if i in fingerprint))