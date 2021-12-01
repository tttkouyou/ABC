a, b = input().split()
a = int(a)
b = int(b)
answer = 4

x = a + b

if x >= 3:
  answer =  answer - 1
  if x >= 10 and b >= 3:
    answer = answer -1
    if x >= 15 and b >= 8:
      answer = answer -1

print(answer)
