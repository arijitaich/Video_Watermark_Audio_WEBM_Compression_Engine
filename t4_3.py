from datetime import datetime
from random import randint
value = randint(0, 10)
now = datetime.now()
dt_string = now.strftime("%d%m%Y%H%M%S") + str(value)
print("date and time =", dt_string)