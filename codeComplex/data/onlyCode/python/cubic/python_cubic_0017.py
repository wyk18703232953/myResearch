import sys
import logging
logging.root.setLevel(level=logging.DEBUG)
import re

s = sys.stdin.readline().strip()

from collections import defaultdict
substr = defaultdict(int)
for left in range(len(s)):
    for right in range(left+1,len(s)+1):
        substr[s[left:right]] += 1
max_len = 0
for segment,times in substr.items():
    if times >= 2:
        max_len = max(max_len,len(segment))
print(max_len)

