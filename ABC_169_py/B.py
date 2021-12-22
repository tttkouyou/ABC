n = input()

a = input().split()

sum = 1

flg = True

if "0" in a:
  flg = False
  print(0)

for i in a:

  if not flg:
    break

  sum = sum * int(i)
  if sum > 1000000000000000000:
    print(-1)
    flg = False
    break

if flg:
  print(sum)
