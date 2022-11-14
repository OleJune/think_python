import time
seconds = time.time()
days = seconds//(60*60*24)
local_time = time.strftime('%H:%M:%S')
print('Current local time is', local_time)
print(int(days), 'days since the epoch')
