x, y ,z = map(int, input().split())

one_parson_size = y + z

if x % one_parson_size >= z:
  print(x // one_parson_size)
else:
  print((x // one_parson_size) - 1)
