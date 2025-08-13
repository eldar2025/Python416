# from car import carclass
#
#
# class ElectroCar(CarClass.CarClass):
#     ...

from car.carclass import CarClass


class ElectroCar(CarClass):
    def __init__(self,brand, model, year, run,battery):
        super().__init__(brand, model, year, run)
        self.battery = battery

    def descript_battery(self):
        print(f"Этот автомобиль имеет мощность {self.battery}%")