import sys
import threading
import time


def a():
    while 1:
        time.sleep(1)

t = threading.Thread(target=a)
t.setDaemon(1)
t.start()
t.join()

sys.exit('goodbye')
sys.exit('goodbye')