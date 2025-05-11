# option 1
# class + instance (obj)
class Car:
    type = 'Toyota'
    model = 'RAV-4'
    color = 'Black'
    speed = 180

if __name__ == '__main__':
    print(Car.type)
    c = Car()
    print(type(c))

