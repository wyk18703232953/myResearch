from sys import stdin, stdout
n = int(stdin.readline())
m = int(stdin.readline())
stdout.write(str(m%(1<<n)))