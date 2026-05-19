import random
import time

class TemperatureSensor:

    def __init__(self, sensor_id, normal, moderate):
        self.sensor_id = sensor_id
        self.count = 0
        self.NORMAL = normal
        self.MODERATE = moderate

    def monitor(self):
        temperature = self.get_temperature()
        self.classifier(temperature)
        time.sleep(2)

    def get_temperature(self):
        try :
            if random.randint(1, 10) == 1:
                raise Exception("Sensor Read Error")
                
            return random.randint(0, 100)
        except Exception as error :
            print(f"{[self.sensor_id]} Sensor Error : {error}")
            return None
        finally :
            pass

    def log_writer(self, temperature):
        try :
            with open("thermal_history.txt", "a") as log_file:
                log_file.write(
                    f"[{self.sensor_id}] {time.strftime('%Y-%m-%d %H:%M:%S')} - Critical Temperature: {temperature}\n"
                )
            self.count += 1
        except OSError as error :
            print(f"Writing error : {error}")
        finally :
            pass

    def log_error(self, message) :
        try :
            with open("thermal_history.txt", "a") as log_file:
                log_file.write(
                    f"[{self.sensor_id}] {time.strftime('%Y-%m-%d %H:%M:%S')} - Found Error : {message}\n"
                )
        except OSError as error :
            print(f"Writing error : {error}")

    def classifier(self, temperature):
        
        if temperature is None:
            self.log_error("Sensor read failed")
            return
        
        if temperature <= self.NORMAL:
            print(f"[{self.sensor_id}] {time.ctime()} : {temperature} C -- Normal")
        elif temperature <= self.MODERATE:
            print(f"[{self.sensor_id}] {time.ctime()} : {temperature} C -- Moderate")
        else:
            print(f"[{self.sensor_id}] {time.ctime()} : {temperature} C -- Critical")
            self.log_writer(temperature)
