
import random

#
'''
#declare lists
engine_num = [] #format ABCD1234
chassis_num = [] #format 12345678
registration_num = [] #UP656789
color = [] #black, white, blue, brown, silver, red

two_wheeler_type = [] #scooter, bike
car_gear_system = [] # manual, automatic
'''

two_wheeler_type_val = {0:'scooter', 1:'bike'}
car_gear_system_value = {0:'manual', 1:'automatic'}
color_value ={0:'black', 1:'white', 2: 'blue', 3:'brown', 4:'silver', 5:'red'}

class VehicleDataGenerator:
    def __init__(self, count):
        self.count = count
        self.engine_num_list = []
        self.chassis_num_list = []
        self.registration_num_list = []
        self.color_list = []
        for i in range(0,count):
            random_engine_num = chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + str(random.randint(1000,9999))
            random_chassis_num = str(random.randint(1000,9999)) + str(random.randint(1000,9999))
            random_registration_num = chr(random.randint(65, 90)) + chr(random.randint(65, 90)) + str(random.randint(40,85)) + str(random.randint(1000,9999))
            random_color = color_value.get(random.randint(0,5))
            # print("engine no: ",random_engine_num,", chassis no: ",random_chassis_num,", reg no ",random_registration_num)
            self.engine_num_list.append(random_engine_num)
            self.chassis_num_list.append(random_chassis_num)
            self.registration_num_list.append(random_registration_num)
            self.color_list.append(random_color)

    def copy_data(self):
        return [self.count,self.engine_num_list,self.chassis_num_list,self.registration_num_list,self.color_list]

    def display_generated_data(self, index):
            print(" Colour :", self.color_list[index])
            print("     Engine no: ",self.engine_num_list[index],", Chassis no: ",self.chassis_num_list[index],", Reg no ",self.registration_num_list[index], end ="\n\n")
            
class TwoWheelerDataGenerator(VehicleDataGenerator):
    def __init__(self, count):
        super().__init__(count)
        self.type_list = []
        for i in range(0,count):
            random_type = two_wheeler_type_val.get(random.randint(0,1))
            self.type_list.append(random_type)

    def copy_data(self):
        list = super().copy_data()
        list.append(self.type_list)
        return list

    def display_generated_data(self):
        for i in range(0,self.count):
            print(" Two wheeler type :", self.type_list[i])
            super().display_generated_data(i)


class CarDataGenerator(VehicleDataGenerator):
    def __init__(self, count):
        super().__init__(count)
        self.gear_system_list = []
        for i in range(0,count):
            random_type = car_gear_system_value.get(random.randint(0,1))
            self.gear_system_list.append(random_type)

    def copy_data(self):
        list = super().copy_data()
        list.append(self.gear_system_list)
        return list

    def display_generated_data(self):
        for i in range(0,self.count):
            print(" Car Gear system :", self.gear_system_list[i])
            super().display_generated_data(i)