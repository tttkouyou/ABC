n, x = input().split()
n = int(n)

list = input().split()
result_list = []

for i in list:
  if i != x:
    result_list.append(i)

print(" ".join(result_list))
