import random

temp = random.uniform(100)

if temp <= 32 :
  print("Normal")
elif temp <= 60 :
  print("Moderate")
else :
  print("Critical")
