# Створити клас, який буде описувати властивості хімічного елементу.
# 1. Для класу має бути описаний метод __init__(...), який приймає два параметри:
# температура плавлення та температура кипіння.
# 2. В класі має бути описаний метод, який в якості аргумента отримує температуру
# (в градусах цельсія) та повертає строку, яка відповідає агрегатному стану речовини при цій температурі.
# 3. Додати в клас метод, який приймає в якості аргументів температуру (число)
# та назву шкали виміру (“C” / “F” / “K”) та конвертує її в градуси цельсія.
# 4. Зробити можливим передавати температуру та шкалу в метод з п.2

class Element:
    def __init__ (self, t_liquid: int, t_gas: int):
        self.t_liquid = t_liquid
        self.t_gas = t_gas

    def check_agg_state(self, C_degr: int, type: str) -> str:
        if type != 'C':
            C_degr = self.degrees_type(C_degr, type)

        if C_degr < self.t_liquid:
            return 'solid'
        elif self.t_liquid < C_degr < self.t_gas:
            return 'liquid'
        else:
            return 'gas'

    def degrees_type(self, C_degr: int, type: str) -> int:
        if type == 'K':
            C_degr -= 273
            return C_degr
        elif type == 'F':
            C_degr = (C_degr - 32) * 0.5555
            return int(C_degr)
        else:
            return C_degr



alum = Element(660, 2470)
water = Element(0, 100)
silicium = Element(1440, 2355)

print('Aluminum in a state of', alum.check_agg_state(498, 'C'), 'with', alum.degrees_type(498, 'C'), '^C')
print('\nWater in a state of', water.check_agg_state(390, 'K'), 'with', water.degrees_type(390, 'K'), '^C')
print('\nSilicium in a state of', silicium.check_agg_state(3500, 'F'), 'with', silicium.degrees_type(3500, 'F'), '^C')

input()