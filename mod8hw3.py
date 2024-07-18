class Car:
    def __init__(self, model: str, vin_number: int, numbers: str):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers
        self.__is_valid_vin()
        self.__is_valid_numbers()

    def __is_valid_vin(self):
        #self.vin_number = vin_number
        #vin_number = self.__vin
        if not (isinstance(self.__vin, int)):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not (1000000 <= self.__vin <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self):
        #self.numbers = numbers
        #numbers = self.__numbers
        if not isinstance(self.__numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif not len(self.__numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message: str):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message: str):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')


try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')