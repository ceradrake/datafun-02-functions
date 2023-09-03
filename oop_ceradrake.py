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

    name2 = "Gypsophilia"
    units2 = "Bunch"
    data2 = "20"
    loc2 = "South America"

    name3 = "Gerbera Daisy"
    units3 = "Stem"
    data3 = "40"
    loc3 = "Denmark"

    object1 = NumericFloralSeries(name1, units1, data1, loc1)
    object2 = NumericFloralSeries(name1, units2, data2, loc2)
    object3 = NumericFloralSeries(name3, units3, data3, loc3)


logger.info(f"Created: {object1}")
logger.info(f"Created: {object2}")
logger.info(f"Created: {object3}")


