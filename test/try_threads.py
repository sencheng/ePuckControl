# -*- coding: utf-8 -*-
"""
Test how threads work.

"""

import threading
import time

class Controller(object):
    def __init__(self, robot):
        self.robot= robot
        self.lock= threading.Lock()
        
    def read_sensor(self,x,y):
#        self.lock.acquire()
        with self.lock:
            time.sleep(1.5)
            print 'read_sensor'        
#        self.lock.release()
        return x+y

    def set_motor(self,x,y):
#        self.lock.acquire()
        with self.lock:
            time.sleep(1.5)
            print 'set_motor'        
#        self.lock.release()
        return x+y

class PathInt(threading.Thread):
    def __init__(self, _control):
        threading.Thread.__init__(self)
        self.control= _control
#        self.daemon= True 
        self.start()
        
    def run(self):
        print 'Starting PathInt...'
#        time.sleep(1)
        print "PI started= %g" %(time.time()-start)        
        z= self.control.read_sensor(1,2)
        print "PI result= %d, finished %g" %(z,time.time()-start)
        
class CollisionAvoidance(threading.Thread):
    def __init__(self, _control):
        threading.Thread.__init__(self)
        self.control= _control
#        self.daemon= True 
        self.start()
        
    def run(self):
        print 'Starting CollisionAvoidance...'
#        time.sleep(.1)
        print "CA started= %g" %(time.time()-start)        
        z= self.control.set_motor(45,9)
        print "CA result= %d, finished %g" %(z,time.time()-start)
        
start= time.time()

c= Controller('epuck')
p= PathInt(c)

#time.sleep(.1)

for i in range(3):
    ca= CollisionAvoidance(c)


#p.join()

print 'program done'

