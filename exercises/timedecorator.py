import random
import time

def timedecorator(func):
    def wrapper(*args,**kwargs):
        t1 = float(time.time())
        func(*args,**kwargs)
        t2 = float(time.time())
        print "Your alogrithm run time is %s" % (t2-t1)
    return wrapper
