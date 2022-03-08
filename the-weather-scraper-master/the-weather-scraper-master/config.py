from datetime import date

# Set Date format like: YYYY, MM, DD
# Note that FIND_FIRST_DATE uses START_DATE as default start date
START_DATE = date(2021, 5, 10)
END_DATE = date(2021, 5, 19)

# set to "metric" or "imperial"
UNIT_SYSTEM = "metric"
# UNIT_SYSTEM = "imperial"

# Automatically find first date where data is logged
FIND_FIRST_DATE = False