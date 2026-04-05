import time

def start_timer(seconds):
    while seconds:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time up!")

start_timer(10)