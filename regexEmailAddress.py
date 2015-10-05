__author__ = 'Robert'



import re
import sys
import io

#emails = []

sin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')
n = int(sin.readline())
text = ''
for ii in range(n):
    text += sin.readline()

    emails = re.findall(r'\b([\w.]+@[\w.]+\.\w+)\b',text)

print(';'.join(sorted(set(emails))))