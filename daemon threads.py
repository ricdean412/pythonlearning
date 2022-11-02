# daemon threads = a thread in the background, not important
# for program to run your program will not wait for daemon threads to complete
# before exiting non daemon threads cannot normally be killed, stay alive until
# if task is complete:

# ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for : ",count, "Seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon())


answer = input("Do you wish to exit?")