import random
import time
import controller

start = time.ctime()

system1 = controller.TemperatureSensor("SNS101", normal = 30, moderate = 60)
system2 = controller.TemperatureSensor("SNS102", normal = 20, moderate = 50)

sensors = [system1, system2]

for sensor in sensors :
    print("System ID : ", sensor.sensor_id)
    for _ in range(random.randint(5, 11)) :
        sensor.monitor()
    print(f"No. of critical incidents from {start} to {time.ctime()} : {sensor.count}")
