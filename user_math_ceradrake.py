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

# Calculate the total value of a floral arrangement 

def value_of_floralarrangement(cost, labor): 
    logger.info(f"CALLING value_of_floralarrangement{cost, labor}")

    try: 
        value = cost * labor
        logger.info(f"The value of the floral arrangment is {value}")
        return value 
    except Exception as ex: 
        logger.error(f"Error: {ex}")
        return None

#Calculate the subtotal of a customer's purchase 

def subtotal_of_customerorder(items_list): 
    logger.info(f"CALLING subtotal_of_customerorder {items_list}")

    try: 
        subtotal = math.fsum(items_list)
        logger.info(f"The subtotal of the customer order is {subtotal:.2f}")
        return subtotal 
    except Exception as ex: 
        logger.error(f"Error: {ex}")
        return None
    
#Calculate the average sale 
        
def average_sale(total_sales, number_of_sales):
    logger.info(f"CALLING average_sale {total_sales, number_of_sales}")

    try: 
        average = total_sales / number_of_sales 
        logger.info(f"The average sale is {average}]")
        return average
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

    logger.info(f"TRY: Call value_of_floralarrangement() function with different values.")
    value_of_floralarrangement(40,1.30)
    value_of_floralarrangement(70,1.35)

    logger.info(f"TRY: Call subtotal_of_customerorder")
    items_list = (20, 2, 3)
    subtotal_of_customerorder(items_list)

    logger.info(f"TRY: Call average_sale")
    average_sale(150, 4)
    average_sale(350, 10)



