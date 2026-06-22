distances = [1, 2, 3, 4, 5]



square_distances = [distance**2 for distance in distances if distance > 3]
print(square_distances)
# -------------------
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


models_of_drones = [drone.model for drone in drones]
print(models_of_drones)