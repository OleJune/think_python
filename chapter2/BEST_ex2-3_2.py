from datetime import time, datetime, date, timedelta
exit_time = time(6, 52)
run_time = datetime.combine(date.today(), exit_time) + timedelta(minutes=8, seconds=15)\
           + timedelta(minutes=8, seconds=15) + timedelta(minutes=7, seconds=12)\
           + timedelta(minutes=7, seconds=12) + timedelta(minutes=7, seconds=12)
return_time = run_time.time()
print('Runner left the house at 6:52 AM.')
print('Runner will get home at', return_time, 'AM.')
