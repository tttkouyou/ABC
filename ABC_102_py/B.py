n = input()
a = input().split()

max = 1

min = float("inf")

for i in a:
  if max <= float(i):
    max = float(i)

  if min >= float(i):
    min = float(i)

print(int(max - min))
