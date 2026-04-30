import random
import time

start = time.ctime()
count = 0
n = random.randint(5, 11)

class TemperatureSensor :
  def __init__(self, id):
    self.sensor_id = id

  def temperature(self) :
    temp = 0
    count = 0

    for i in range(n) : 
    
      temp = random.randint(0, 100)
  
    if temp <= 32 :
      print(f"{time.ctime()} : {temp} C -- Normal")
    elif temp <= 60 :
      print(f"{time.ctime()} : {temp} C -- Moderate")
    else :
      print(f"{time.ctime()} : {temp} C -- Critical")
      with open("log.txt", "a") as log_file :
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Critical Temperature: {temp}\n")
      count += 1 # not being counted 

    time.sleep(2)

  print(f"No.of critical incidents from {start} to {time.ctime()} : {count}")


system1 = TemperatureSensor(1)
print("System ID : ", system1.sensor_id)
for i in range(n) : 
  system1.temperature()
