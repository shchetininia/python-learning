drone = {"масса": 5, "модель": "Skywalker X-8", "максимальная высота": 5000}
drone["скорость"] = 20

for key, value in drone.items():
    print(f"{key}: {value}")

# drone["несуществующий ключ"]