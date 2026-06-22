drones = {"Дрон1":{"масса": 5, "модель": "Skywalker X-8", "максимальная высота": 5000, },
         "Дрон2":{"масса": 6, "модель": "Skywalker X-9", "максимальная высота": 6000, "скорость": 20 },
         "Дрон3":{"масса": 7, "модель": "Skywalker X-10", "максимальная высота": 7000, "скорость": 25, "мощность": 45 },
         "Дрон4":{"масса": 8, "модель": "Skywalker X-11"}}
# for key1,drone in drones.items():
#     for key,value in drone.items():
#         print(f"{key1} -> {key}: {value}")
name = input("Напиши имя дрона: ")
characteristic = input("Напиши характеристику дрона: ")
try:
    print(f" Ваш дрон: {name}, Характеристика: {drones[name][characteristic]}")
except KeyError as e:
    print("Такого дрона или характеристики не существует")
    print(f"Ошибка: {e}")
