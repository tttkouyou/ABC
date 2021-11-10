n, s, d = input().split()
n = int(n)
s = int(s)
d = int(d)

flg = False

for i in range(n):
  x, y = input().split()
  x = int(x)
  y = int(y)

  if x < s and y > d:
    flg = True

if flg:
  print("Yes")
else:
  print("No")
