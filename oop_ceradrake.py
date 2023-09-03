from util_logger import setup_logger
logger, logname = setup_logger(__file__)

from numeric_series import NumericSeries

class NumericFloralSeries(NumericSeries) :
    """ A class that represents numeric data customized for the floral industry"""

    def __init__(self, name, units, data):
        super().__init__(name, units, data)
    def __str__(self):
        return super().__str__()
    
        str = f"NumericFloralSeries with name={self.name}, units={self.units}, location={self.location}, and {len(self.data)} data points: {self.data}"
        return str

if __name__ == "__main__":
    name1 = "Alstromeria Lily"
    units1 = "Bunch"
    data1 = "10"
    loc1 = "South America"

    object1 = NumericFloralSeries(name1, units1, data1, loc1)



