s = input()

i = 1
answer = ""

while i < len(s):
  answer = answer + s[i]
  i = i + 1

answer = answer + s[0]

print(answer)
