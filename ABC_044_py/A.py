n = int(input())
k = int(input())
x = int(input())
y = int(input())

answer = 0

if k < n:
  n = n - k
  answer = x * k
  answer = answer + (n * y)
else:
  answer = n * x

print(answer)
