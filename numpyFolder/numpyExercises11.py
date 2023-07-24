import numpy as np
#DataTime
#1
# print(np.arange('2017-03', '2017-04', dtype='datetime64[D]'))
#2
# yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
# today = np.datetime64('today', 'D')
# tomorrow = np.datetime64('today','D') + np.timedelta64(1,'D')
# print(tomorrow)
#3
# print(np.datetime64('2016-03-01') - np.datetime64('2016-02-01'))
#4
# import datetime
# start = datetime.datetime(2000, 1, 1)
# arr = np.array([start + datetime.timedelta(hours=i) for i in range(24)])
# print(arr)
#5
# print(np.busday_offset('2017-05', 0, roll='forward', weekmask='Mon'))
#6
# print(np.busday_count('2017-03-01','2017-04-01'))
#7
# import datetime
# nowDay = datetime.datetime.utcnow()
# arr = np.datetime64(nowDay)
# ts = (arr - np.datetime64('1970-01-01T00:00:00Z'))/np.timedelta64(1,'s')
# print(ts)