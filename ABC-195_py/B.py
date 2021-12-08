A, B, W = map(int, input().split())

min = (W*1000 + B-1) // B
max = (W*1000) // A

if min > max:
    print("UNSATISFIABLE ")
else:
    print(str(min) + " " + str(max))
