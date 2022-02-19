from datetime import datetime

class Record:
  def __init__(self, amount, comment, date=datetime.now()):
    self.amount = amount
    self.date =  date if isinstance(date, datetime) else datetime.strptime(date, '%d.%m.%Y')
    self.comment = comment


class Calculator:
  def __init__(self, limit=0):
    self.records = []
    self.limit = limit

  def add_record(self, record):
    self.records.append(record)

  def get_today_stats(self):
    sum = 0

    for rec in self.records:
      if rec.date.day == datetime.now().day:
        sum += rec.amount

    return sum

  def get_week_stats(self):
    sum = 0
    today = datetime.now().days
    last_week = today - 7

    for rec in self.records:
      if last_week >= rec.day:
        sum += rec.amount 

    return sum


class CaloriesCalculator(Calculator):
  def get_calories_remained(self):
    wasted = self.get_today_stats()
    diff = self.limit - wasted
    if diff > 0 :
      return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {diff} кКал'
    
    else :
      return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {diff} кКал'


class CashCalculator(Calculator):
  def __init__(self, limit):
    super().__init__(limit)
    self.CUR = {
      'rub': 1,
      'usd': 1/80,
      'eur': 1/90 
    }

  def get_today_cash_remained(self, currency):
    coef = self.CUR[currency]
    wasted = self.get_today_stats()
    diff = self.limit - wasted
    if diff > 0 :
      return f'На сегодня осталось {diff * self.CUR[currency]} {currency}'
    elif diff == 0:
      return f'Денег нет, держись'
    else :
      return f'Денег нет, держись, долг: {diff * self.CUR[currency]} {currency}'




cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))
