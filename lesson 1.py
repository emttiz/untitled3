class Car:
    def __init__(self, the_model, the_color, the_year):
        self.model = the_model
        self.color = the_color
        self.year = the_year


num_1 = 45
bmw_car = Car("BMW X6", "Black", 2020)
print(f'Model: {bmw_car.model} Color: {bmw_car.color} Year: {bmw_car.year}')
bmw_car.color = 'Red'
print(f'Model: {bmw_car.model} Color: {bmw_car.color} Year: {bmw_car.year}')