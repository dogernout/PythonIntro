import sys


n = int(input())
s = sys.stdin.read().replace("\n    ", " @ ").split()
s = ' '.join(s[:n])
s = s.replace(" @ ", "\n    ")
print(s)
