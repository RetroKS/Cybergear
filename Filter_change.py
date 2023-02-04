from datetime import date
from dateutil.relativedelta import relativedelta



K5 = relativedelta(months=+6)
K2 = relativedelta(months=+6)
K7M = relativedelta(months=+18)
K_100S = relativedelta(months=+24)

print("Test")

six_months = date.today() + K7M
print(six_months)

