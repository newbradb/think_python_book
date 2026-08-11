from datetime import datetime
from time import time


now = time()
current_time = datetime.now()

seconds_in_day = (60 * 60) * 24
days_since_unix_epoch = now / seconds_in_day

print('There are ', round(days_since_unix_epoch),  ' days since unix epoch')
print(current_time.strftime('%d, %H:%M:%S'))







