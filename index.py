import random
import time

start = time.ctime()

class TemperatureSensor :
  def __init__(self, id):
    self.sensor_id = id
    self.count = 0

  def temperature(self) :
    temp = 0
    
    temp = random.randint(0, 100)
  
    if temp <= 32 :
      print(f"{time.ctime()} : {temp} C -- Normal")
    elif temp <= 60 :
      print(f"{time.ctime()} : {temp} C -- Moderate")
    else :
      print(f"{time.ctime()} : {temp} C -- Critical")
      with open("log.txt", "a") as log_file :
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Critical Temperature: {temp}\n")
      self.count += 1

    time.sleep(2)

system1 = TemperatureSensor(1)
print("System ID : ", system1.sensor_id)
for i in range(5, 11) : 
  system1.temperature()

print(f"No. of critical incidents from {start} to {time.ctime()} : {system1.count}")
