class Drone:
    def __init__(self, mass, model, max_height, speed = 0):
        self.mass = mass
        self.model = model
        self.max_height = max_height
        self.speed = speed
    def describe(self):
        return f"Масса: {self.mass}, Модель: {self.model}, Максимальная высота: {self.max_height}, Скорость: {self.speed}"


drone1 = Drone(5,"Skywalker X-8",5000, 20)
drone2 = Drone(6,"Skywalker X-9",6000, 25)
drone3 = Drone(7,"Skywalker X-10",5000)

drones = [drone1,drone2,drone3]
for drone in drones:
    print(drone.describe())

# point = (1,2,3)
# # point[0] = 99
# models_list = ["X-8", "X-9", "X-8", "X-10"]
# unique = set(models_list)
# print(unique)

# --------------------
print("Чтение файла. Задание.")
with open("drones_log.txt", "w",encoding="utf-8") as f:
    for drone in drones:
        f.write(drone.describe() + "\n")

with open("drones_log.txt", "r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())
