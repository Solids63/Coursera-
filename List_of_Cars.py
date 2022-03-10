import csv
import os


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename, encoding='UTF8') as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0]:
                    car_list.append(row)
            except:
                continue
    for car in car_list:
        print(car)
        if car[0] == 'car':
            Car(brand=car[1], photo_file_name=car[3], carrying=car[5], passenger_seats_count=car[2])
        elif car[0] == 'truck':
            Truck(brand=car[1], photo_file_name=car[3], carrying=car[5], body_whl=car[4])
        elif car[0] == 'spec_machine':
            SpecMachine(brand=car[1], photo_file_name=car[3], carrying=car[5], extra=car[6])
    return car_list



class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
#        self.get_photo_file_ext()

#    def get_photo_file_ext(self):
#        path = 'C:/Users/yk63/Python/Coursera/MFTI/coursera_week3_cars.csv/photo_file_name'
#        name = os.path.splitext(path)
#        print(name)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count=None, ):
        self.passenger_seats_count = passenger_seats_count
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'

    def outcome(self):
        return self.brand, self.photo_file_name, self.carrying, self.passenger_seats_count, self.car_type


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        self.car_type = 'truck'
        if body_whl:
            limits = self.body_whl.split('x')
            for limit in limits:
                if limit in limits is not None:
                    self.body_width = float(limits[0])
                    self.body_height = float(limits[1])
                    self.body_length = float(limits[2])
                else:
                    self.body_width = 0
                    self.body_height = 0
                    self.body_length = 0
        else:
            self.body_width = 0
            self.body_height = 0
            self.body_length = 0

        self.get_body_volume()
    def outcome(self):
        return self.car_type, self.brand, self.photo_file_name, self.carrying, self.body_whl, self.body_width, self.body_height, self.body_length

    def get_body_volume(self):
        body_volume = self.body_width*self.body_length*self.body_height
        return body_volume


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'

    def outcome(self):
        return self.brand, self.photo_file_name, self.carrying, self.extra, self.car_type


cars = get_car_list('coursera_week3_cars.csv')
print(len(cars))
for car in cars:
    print(type(car))

#  print(cars[0].passenger_seats_count)
#  truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
#  print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')

#  car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
#  print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')

#  spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
#  print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
print(isinstance(Car, CarBase))
