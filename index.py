import random

count = 0

for i in range(10) : 
    
  temp = random.uniform(100)
  
  if temp <= 32 :
    print("Normal")
  elif temp <= 60 :
    print("Moderate")
  else :
    print("Critical")
    count += 1

print("No.of critical incidents : ", count)
