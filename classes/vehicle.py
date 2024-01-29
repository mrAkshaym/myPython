

class Vehicle:
    def __init__(self, engine_num, chassis_num, registration_num, color):
        self.engine_num = engine_num
        self.chassis_num = chassis_num
        self.registration_num = registration_num
        self.color = color

    def display_info(self):
        print("Engine number :", self.engine_num)
        print("Chassis number :", self.chassis_num)
        print("Registration number :", self.registration_num)

class TwoWheeler(Vehicle):
    def __init__(self,engine_num, chassis_num, registration_num, color, type):
        super().__init__(engine_num, chassis_num, registration_num, color)
        self.type = type

    def display_info(self):
        print("Two wheeler vehicle type is", self.type)
        super().display_info()

class Car(Vehicle):
    def __init__(self,engine_num, chassis_num, registration_num, color, gear_system):
        super().__init__(engine_num, chassis_num, registration_num, color)
        self.gear_system = gear_system