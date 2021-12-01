# 販売軒数
n = input()
n = int(n)

min = 999999999999999

for i in range(n):
  a, p, x = input().split()
  # A:徒歩での時間（分）
  a = int(a)

  # P:販売価格
  p = int(p)

  # X:在庫
  x = int(x)

  if a < x:
    if p < min:
      min = p

if min == 999999999999999:
  print(-1)
else:
  print(min)
