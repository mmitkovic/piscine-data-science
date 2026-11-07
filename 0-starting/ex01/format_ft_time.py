import time
from datetime import date

seconds = time.time()
scientific_format = "{:.2e}".format(seconds)
print(f"Second since January 1, 1970: {seconds:,.4f} or {scientific_format} in scientific notation")

now = date.today()
month = now.strftime("%B")
day_year = now.strftime("%d %Y")
print(f"{month[:3]} {day_year}")

