v, t, s, d = input().split()
v = int(v)
t = int(t)
s = int(s)
d = int(d)

ballTime = d / v

if(ballTime >= t and ballTime <= s):
  print("No")
else:
  print("Yes")
