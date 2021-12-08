h, w, x, y = map(int, input().split())
x -= 1
y -= 1

s = []

for i in range(h):
  s.append(list(input()))

i, j = x+1, y
answer = 0

while i < h and s[i][j] != "#":
  i += 1
  answer += 1

i, j = x-1, y
while i >= 0 and s[i][j] != "#":
  i -= 1
  answer += 1

i, j = x, y+1
while j < w and s[i][j] != "#":
  j += 1
  answer += 1

i, j = x, y-1
while j >= 0 and s[i][j] != "#":
  j -= 1
  answer += 1

print(answer+1)
