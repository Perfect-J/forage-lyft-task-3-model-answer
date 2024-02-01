from battery.battery import Battery
from utils import add_years_to_date


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

# Assuming this is part of your existing test class
class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced_after_three_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Spindler(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

