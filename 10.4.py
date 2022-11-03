# Write a Race class that has the
# following properties: name, distance in kilometers and a list of cars participating in the race. The class has an
# initializer that receives the name, kilometers, and car list as parameters and sets their values to the
# corresponding properties in the class. The class has the following methods:
#
# hour_passes, which performs the operations done once per hour in the original exercise: generates a random change
# of speed for each car and calls their drive method. print_status, which prints out the current information of each
# car as a clear, formatted table. race_finished, which returns True if any of the cars has reached the finish line,
# meaning that they have driven the entire distance of the race. Write a main program that creates an 8000-kilometer
# race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The
# main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the
# race_finished method to check if the race has finished. The current status is printed out using the print_status
# method every ten hours and then once more at the end of the race.

import random
from texttable import Texttable


# a Car class that has the following properties: registration number, maximum speed, current speed and
# travelled distance.
class Car:
    # class initializer that sets the first two of the properties based on parameter values. The current speed and
    # travelled distance of a new car are automatically set to zero.
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = 0
        self.travel_dist = 0

    # accelerate method, that receives the change of speed (km/h) as a parameter. If the change is negative,
    # the car reduces speed. The speed of the car is set below maximum and is not less than zero.
    def accelerate(self, change_of_speed):
        self.curr_speed = self.curr_speed + change_of_speed
        if change_of_speed >= 0:
            if self.curr_speed > car.max_speed:
                self.curr_speed = car.max_speed
            # print(f"The car has accelerated {change_of_speed} km/h.")
        if change_of_speed < 0:
            if self.curr_speed < 0:
                self.curr_speed = 0
            # print(f"The car has decelerated {change_of_speed} km/h.")

    # drive method that receives the number of hours as a parameter. The method increases the travelled distance by
    # how much the car has travelled in constant speed in the given time.
    def drive(self, num_of_hours):
        self.travel_dist = self.travel_dist + (self.curr_speed * num_of_hours)
        return self.travel_dist
        # print(f"The travelled distance is now {car.travel_dist} km.\n")


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    # generates a random change of speed for each car and calls their drive method.
    def hour_passes(self):
        self.hour = 0
        self.hour += 1
        for i in range(len(self.cars)):
            self.cars[i].accelerate(random.randint(-10, 15))
            self.cars[i].drive(1)
            if self.hour % 10 == 0:
                self.print_status()
        '''
        while car.travel_dist < self.distance:
            hour += 1
            for i in self.cars:
                self.race_finished()
                car.accelerate(random.randint(-10, 15))
                car.drive(1)
                if hour % 10 == 0:
                    self.print_status()
        '''

    # prints out the current information of each car as a clear, formatted table
    def print_status(self):
        table = Texttable()
        table.header(["registration number", "maximum speed", "current speed", "travelled distance"])
        for i in self.cars:
            table.add_row([car.reg_num, car.max_speed, car.curr_speed, car.travel_dist])
        print(table.draw())

    # returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance
    # of the race.
    def race_finished(self):
        if car.travel_dist > self.distance:
            print("Tha race is finished!")
            self.print_status()
            return True


cars = []
num = 0
while num < 10:
    num += 1
    car = Car(f"ABC-{num}", random.randint(100, 200))
    cars.append(car)
    print(f"The car with {car.reg_num} is created, the maximum speed is {car.max_speed} km/h.")

race1 = Race("Grand Demolition Derby", 8000, cars)
while True:
    race1.hour_passes()
    if race1.race_finished()==True:
        break
