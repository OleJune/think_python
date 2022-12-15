import time
seconds = time.time()
minutes = seconds/60
hours = minutes/60
days = hours/24
current_hrs = hours % 24
current_min = minutes % 60
current_sec = seconds % 60
sign = ':'

print(int(days), 'days since the epoch')

print(str(int(current_hrs))+sign+str(int(current_min))+sign+str(int(current_sec)), 'GMT')