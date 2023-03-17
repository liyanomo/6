import time
from threading import Thread


def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


for i in range(5):
    get_thread(i + 1)