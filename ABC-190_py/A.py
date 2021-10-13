a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > b:
  print("Takahashi")

elif a < b:
  print("Aoki")

elif a == b and c == 0:
  print("Aoki")

elif a == b and c == 1:
  print("Takahashi")
