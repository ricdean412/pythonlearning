from car import Car

car_1 = Car("BMW","M3","2018","White")
car_2 = Car("Benz","S580","2022","Black")

Car.wheels = 2

print("There is only "+str(car_1.wheels)+" wheels on this vehicle!")
print(car_2.wheels)