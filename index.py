import random
import time

start = time.ctime()

class TemperatureSensor :
    
  NORMAL = 32
  MODERATE = 60
    
  def __init__(self, id):
      self.sensor_id = id
      self.count = 0

  def get_temperature(self) :
      
    self.temp = random.randint(0, 100)

  def log_writer(self) :
      with open("log.txt", "a") as log_file :
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Critical Temperature: {self.temp}\n")
      self.count += 1

  def classifier(self) :
    
    if self.temp <= self.NORMAL : 
        print(f"{time.ctime()} : {self.temp} C -- Normal")
    elif (self.temp <= self.MODERATE) : 
        print(f"{time.ctime()} : {self.temp} C -- Moderate")
    else :
        print(f"{time.ctime()} : {self.temp} C -- Critical")
        self.log_writer()

  def monitor(self) :
    
    self.get_temperature()
    
    self.classifier()
    
    time.sleep(2)

system1 = TemperatureSensor(1)
print("System ID : ", system1.sensor_id)
for i in range(5, 11) : 
  system1.monitor()

print(f"No. of critical incidents from {start} to {time.ctime()} : {system1.count}")
