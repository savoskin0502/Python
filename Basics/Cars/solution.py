import sys
import csv
import os


class CarBase:
    
    car_type = 0
    brand = 1
    passenger_seats_count = 2
    photo_file_name = 3
    body_whl = 4
    carrying = 5
    extra = 6

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    
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
            car[cls.brand],
            car[cls.photo_file_name],
            car[cls.carrying],
            car[cls.passenger_seats_count]
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
            truck[cls.brand],
            truck[cls.photo_file_name],
            truck[cls.carrying],
            truck[cls.body_whl]
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
            spec[cls.brand],
            spec[cls.photo_file_name],
            spec[cls.carrying],
            spec[cls.extra]
        )


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        car_classes = {car.car_type: car for car in (Car, Truck, SpecMachine)}

        for row in reader:
            try:
                car_type = row[CarBase.car_type]
            except IndexError:
                continue
            try:
                car_class = car_classes[car_type]
                # print(car_class)
            except KeyError:
                continue
            
            try:
                car_list.append(car_class.instance(row))
            except (IndexError, ValueError):
                pass
    
    return car_list
