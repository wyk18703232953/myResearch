import re
input()
print(sum(len(f)-2 for f in re.findall('x{3,}',input())))