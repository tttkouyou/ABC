n = input()

zeroAdd_text = n

list_alpha = []
list_beta = []

flg = True

for i in range(1, len(n)):
  if(n[-i] == "0"):
    zeroAdd_text = "0" + zeroAdd_text
  else:
    break

for i in range(len(zeroAdd_text)//2):
  if(zeroAdd_text[i] != zeroAdd_text[-(i+1)]):
    flg = False
    break

if(flg):
  print("Yes")
else:
  print("No")
