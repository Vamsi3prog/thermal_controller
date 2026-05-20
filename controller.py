import random
import time

class TemperatureSensor:

    def __init__(self, sensor_id, normal, moderate):
        if normal >= moderate:
            raise ValueError("normal must be less than moderate")
        
        self.sensor_id = sensor_id
        self.count = 0
        self.normal = normal
        self.moderate = moderate

    def monitor(self):
        temperature = self.get_temperature()
        self.temperature_classifier(temperature)
        time.sleep(2)

    def get_temperature(self):
        try :
            if random.randint(1, 10) == 1:
                raise Exception("Sensor Read Error")
                
            return random.randint(0, 100)
        except Exception as error :
            print(f"[{self.sensor_id}] Sensor Error : {error}")
            return None

    def log_writer(self, temperature):
        try :
            with open("thermal_history.txt", "a") as log_file:
                log_file.write(
                    f"[{self.sensor_id}] {time.strftime('%Y-%m-%d %H:%M:%S')} - Critical Temperature: {temperature}\n"
                )
            self.count += 1
        except OSError as error :
            print(f"Writing error : {error}")

    def log_error(self, message) :
        try :
            with open("thermal_history.txt", "a") as log_file:
                log_file.write(
                    f"[{self.sensor_id}] {time.strftime('%Y-%m-%d %H:%M:%S')} - Found Error : {message}\n"
                )
        except OSError as error :
            print(f"Writing error : {error}")

    def temperature_classifier(self, temperature):
        
        if temperature is None:
            self.log_error("Read cycle failed")
            return
        
        if temperature <= self.normal:
            print(f"[{self.sensor_id}] {time.ctime()} : {temperature} C -- Normal")
        elif temperature <= self.moderate:
            print(f"[{self.sensor_id}] {time.ctime()} : {temperature} C -- Moderate")
        else:
            print(f"[{self.sensor_id}] {time.ctime()} : {temperature} C -- Critical")
            self.log_writer(temperature)
