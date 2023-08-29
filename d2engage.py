"""

Purpose: Illustrate the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpreter
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

"""
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

dataa = [10, 11, 14, 20, 20, 20, 22, 24, 28, 31]

datab = [2, 9, 13, 14, 20, 20, 24, 26, 32, 40]

mean_dataa = statistics.mean(dataa)
median_dataa = statistics.median(dataa)
mode_dataa = statistics.mode(dataa)

mean_datab = statistics.mean(datab)
median_datab = statistics.median(datab)
mode_datab = statistics.mode(datab)

logger.info(f"Data A Mean is {mean_dataa}")
logger.info(f"Data A median is {median_dataa}")
logger.info(f"Data A mode is {mode_dataa}")

logger.info(f"Data B mean is {mean_datab}")
logger.info(f"Data B median is {median_datab}")
logger.info(f"Data B mode is {mode_datab}")





