class Car:
    def __init__(self, car_make, max_speed):    # This is how you feed arguments into a class
        self.car_make = car_make                # NB the car_make on LHS is NOT the same as car_make RHS
        self.max_speed = max_speed              # The self.variables are now class variables
        self.current_speed = 0

    def increase_speed(self, speed_increase):
        if self.current_speed + speed_increase > self.max_speed:
            print(f"Woah there cowboy, your car can't go any faster than {self.max_speed} mph")
            self.current_speed = self.max_speed
        else:
            self.current_speed += speed_increase
            print(f"Vroom! Car now going {self.current_speed} mph")


my_car = Car("Ford", 180)                       # Creating an instance of a car - ie my_car is now a car

my_car.increase_speed(25)
my_car.increase_speed(25)
my_car.increase_speed(25)
my_car.increase_speed(25)
my_car.increase_speed(25)
my_car.increase_speed(25)
my_car.increase_speed(25)
my_car.increase_speed(25)