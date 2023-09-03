# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys

print("Years in business vs. Gross Sales")

years = [1, 2, 3, 4]

grossales = [140000, 130000, 155000, 176000]

mean_years = statistics.mean(years)
median_years = statistics.median(years)
mode_years = statistics.mode(years)

mean_grossales = statistics.mean(grossales)
median_grossales = statistics.median(grossales)
mode_grossales = statistics.mode(grossales)

logger.info(f"Years in business Mean is {mean_years}")
logger.info(f"Years in business median is {median_years}")
logger.info(f"Years in business mode is {mode_years}")

logger.info(f"Gross sales mean is {mean_grossales}")
logger.info(f"Gross sales median is {median_grossales}")
logger.info(f"Gross sales mode is {mode_grossales}")

