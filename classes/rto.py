from vehicle_data_generation import TwoWheelerDataGenerator, CarDataGenerator
from vehicle import TwoWheeler, Car
import random

rto_records_two_wheeler = []
rto_records_cars = []

def rto():

    two_wheeler_engine_num = [] #format ABCD1234
    two_wheeler_chassis_num = [] #format 12345678
    two_wheeler_registration_num = [] #UP656789
    two_wheeler_color = [] #black, white, blue, brown, silver, red
    two_wheeler_type = [] #scooter, bike

    car_engine_num = [] #format ABCD1234
    car_chassis_num = [] #format 12345678
    car_registration_num = [] #UP656789
    car_color = [] #black, white, blue, brown, silver, red
    car_gear_system = [] # manual, automatic

    two_wheeler_count = int(input(" Enter num of two-wheelers."))
    car_count = int(input(" Enter num of cars."))

    two_wheeler_data = TwoWheelerDataGenerator(two_wheeler_count)
    car_data = CarDataGenerator(car_count)

    two_wheeler_data.display_generated_data()
    count = 0
    list = []
    list = two_wheeler_data.copy_data()
    for i in range (0, list[0]):
        rto_records_two_wheeler.append(TwoWheeler(list[1][i],list[2][i], list[3][i],list[4][i],list[5][i] ))


    car_data.display_generated_data()
    count = 0
    list = []
    list = car_data.copy_data()
    for i in range (0, list[0]):
        rto_records_cars.append(Car(list[1][i],list[2][i], list[3][i],list[4][i],list[5][i] ))
    
def main():
    rto()

    print("=============printing some random records. ====================")

    #display random records
    two_wheeler_count = rto_records_two_wheeler.__len__()
    for i in range (0,3):
        random_index = random.randint(0,(two_wheeler_count-1))
        print(" Random 2-wheeler index = ",random_index )
        rto_records_two_wheeler[random_index].display_info()

    for i in range (0,3):
        cars_count = rto_records_cars.__len__()
        random_index = random.randint(0,(cars_count-1))
        print(" Random car index = ",random_index )
        rto_records_cars[random_index].display_info()
        

main()

