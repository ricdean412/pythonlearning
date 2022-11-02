# import time

# print(time.ctime(1000000))    # convert a time expressed in secs since epoch
                        # to a readable string. Epoch = when your computer
                        # thinks time began
# print(time.time())   # return current seconds

# print(time.ctime(time.time())) # creates readable date and time
# time_object = time.localtime()
# time_object = time.gmtime() #UTC Time
# print(time_object)

# time.strftime("format", time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# time_string = time.mktime(time_tuple) #epich
# print(time_string)