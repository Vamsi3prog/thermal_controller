import random
import time

count = 0

for i in range(10) : 
    
  temp = random.uniform(0, 100)
  
  if temp <= 32 :
    print("Normal")
  elif temp <= 60 :
    print("Moderate")
  else :
    print("Critical")
    with open("log.txt", "a") as log_file :
        log_file.write(time.time(), "Critical Temperature : ", temp)
    count += 1

  time.sleep(2)

print("No.of critical incidents : ", count)
