""" Cera Drake 9/2/2023 This module will represent math in the floral industry using defensive math examples from module 2"""
import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)


# calculate the area of a floral arrangement packing box #

def get_area_of_packingbox(height,width): 
    logger.info(f" CALLING get_area_of_packingbox{height,width}")

    try: 
        area = height * width
        logger.info (f"The area of a packing box is {area}")
        return area 
    except Exception as ex: 
        logger.error(f"Error: {ex}")
        return None


if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

    logger.info(f"TRY: Call get_area_of_packingbox() function with different values.")
    get_area_of_packingbox(6,4)
    get_area_of_packingbox(12,18)
    get_area_of_packingbox(10,10)
    
