import sys
import csv
import os


class CarBase:
    
    col_car_type = 0
    col_brand = 1
    col_passenger_seats_count = 2
    col_photo_file_name = 3
    col_body_whl = 4
    col_carrying = 5
    col_extra = 6

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    
    def get_photo_file_ext(self):
        return (os.path.splitext(self.photo_file_name)[1])


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        # self.car_type = 'car'

    @classmethod
    def instance(cls, car):
        return cls(
            car[cls.col_brand],
            car[cls.col_photo_file_name],
            car[cls.col_carrying],
            car[cls.col_passenger_seats_count]
        )

class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            l, w, h = (float(side) for side in body_whl.split('x', 2))
        except ValueError:
            l, w, h = .0, .0, .0
        self.body_length = l
        self.body_width = w
        self.body_height = h
        # self.body_whl =  body_whl
        # self.car_type = 'truck'

    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length
    
    @classmethod
    def instance(cls, truck):
        return cls(
            truck[cls.col_brand],
            truck[cls.col_photo_file_name],
            truck[cls.col_carrying],
            truck[cls.col_body_whl]
        )


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        # self.car_type = 'spec_machine'
    
    @classmethod
    def instance(cls, spec):
        return cls(
            spec[cls.col_brand],
            spec[cls.col_photo_file_name],
            spec[cls.col_carrying],
            spec[cls.col_extra]
        )


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        car_classes = {car.car_type: car for car in (Car, Truck, SpecMachine)}

        for row in reader:
            try:
                car_type = row[CarBase.col_car_type]
            except IndexError:
                continue
            try:
                car_class = car_classes[car_type]
            except KeyError:
                continue
            
            try:
                car_obj = car_class.instance(row)
                if (car_obj.get_photo_file_ext() in ('.jpg', '.jpeg', '.png', '.gif')):
                    arr = list(vars(car_obj).values())
                    nil = [e for e in arr if e!='']
                    if (len(arr)==len(nil)):
                        car_list.append(car_obj)
            except (IndexError, ValueError):
                pass
    return car_list
