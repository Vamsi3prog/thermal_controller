import random
import time

start = time.ctime()
count = 0

for i in range(5) : 
    
  temp = random.randint(0, 100)
  
  if temp <= 32 :
    print(f"{time.ctime()} : {temp} C -- Normal")
  elif temp <= 60 :
    print(f"{time.ctime()} : {temp} C -- Moderate")
  else :
    print(f"{time.ctime()} : {temp} C -- Critical")
    with open("log.txt", "a") as log_file :
        log_file.write(f"{time.strftime("%Y-%m-%d %H:%M:%S")} Critical Temperature : {temp}")
    count += 1

  time.sleep(2)

print(f"No.of critical incidents from {start} to {time.ctime()} : {count}")
