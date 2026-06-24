class Robot:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} двигается"

class FlyingRobot(Robot):
    def __init__(self,name,altitude):
        super().__init__(name)
        self.altitude = altitude
    def move(self):
        return f"{self.name} летит на высоте {self.altitude}"

nameOfARobot = "Terminator"

terminator = Robot(nameOfARobot)

nameOfAFlyingRobot = "Megatron"
altitude = 10000
megatron = FlyingRobot(nameOfAFlyingRobot, altitude)

print(terminator.move())
print(megatron.move())
