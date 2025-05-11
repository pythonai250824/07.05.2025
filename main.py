from car import Car
from vehicle.motorcycle import *

print(Car.speed)
print(Motorcycle.hand_breaks)

print(Car.__dict__)  # dunder

# reflection

# class
class Point:
    pass

# option 2
p1 = Point()  # instance-obj
p2 = Point()  # instance-obj
p1.x = 100
p1.y = 200

p2.x = 100
p2.y = 200

# p3 = p1 + p2  # __add__

class MobilePhone:
    pass

# option 2
samsungS25 = MobilePhone()
iphone16pro = MobilePhone()


# Targil:
# 1
class Movie:
    title = "Thunderbolts"
    year = 2025
    actor = "Florence Pugh"

print(Movie.title)
print(Movie.__dict__)

matrix = Movie()

# create Movie class of your favorite movie:
# [class-instance]
#    title
#    year
#    actor
# 2
# class TV empty  # like point
# create samsung, lg tvs

class TV:
    pass

lg = TV()
samsung = TV()
sharp = TV()

print(type(5))  # <class 'int'>
print(type(sharp))  # <class '__main__.TV'>
print(type(Car))  # <class '__main__.TV'>
c = Car()
print(type(c))
