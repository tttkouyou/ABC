n  = input()
n = int(n)

list = []
m = 1_000_000

for i in range(n):
  a, b = input().split()
  a = int(a)
  b = int (b)
  list.append([a,b])

for j in range(n):
  for k in range(n):
    if j != k:
      max_num = max(list[j][0], list[k][1])
      m = min(m, max_num)
    else:
      m = min(m, list[j][0]+list[j][1])

print(m)
