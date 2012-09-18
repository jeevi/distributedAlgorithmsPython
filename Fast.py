

#---------------------------------Lamport's Fast mutual exclusion algorithm------------------------------------------#

import threading
import time
import logging
import random
# global variables
x = 0
y = -1
totalRequests = 0
Threads = []
runningThreads = []
B = [0]*100

# using the logging module from python's library which basically formats the output to be displayed on the console
logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s, %(asctime)s, %(message)s]', datefmt = '%Y-%m-%d %H:%M:%S')

class Fast(threading.Thread):
    
    # the constructor which assigns the requests, threadname, index to the respective thread
    def __init__(self, string, i, z):
        
        self.threadName = string+str(i)
        self.index = i
        self.requests = z
        threading.Thread.__init__(self, name=self.threadName)
        
    #invoked after the thread.start()
    def run(self):
        logging.debug('is started ... ')
        
        # calling a global function which handles the number of requests of each thread, decrements its value by 1 after entering and exiting a CS once.
        requestManager(self)
        
           
def requestManager(self):
    
    # total requests as entered by the user i.e. sys.argv[2]
    global totalRequests
    # keep doing until all the requests of all the threads have been satisfied 
    while totalRequests > 0:
        #if all the requests are satisfied - do nothing
        if self.requests == 0:
            pass
        # else do this
        else:   
            contend(self)
        totalRequests-=1
        
# a global function which contains the logic of the lamport's fast mutual exclusion algorithm      
def contend(self):

    global y
    global x
    
    logging.debug('requesting CS')
    
    B[self.index] = 1
    x = self.index
    logging.debug('...')
    if y != -1:
        logging.debug('...')
        B[self.index] = 0
        while(not( y == -1)):
            logging.debug("...")
        contend(self)
    y = self.index
    logging.debug('...')
    if x != self.index:
        logging.debug('...')
        B[self.index] = 0
        for each in Threads:
            while(not( B[each.index] == 0)):
                logging.debug("...")
        if y != self.index:
            logging.debug('...')
            while(not( y == -1)):
                logging.debug("...")
            contend(self)
    cs()
    logging.debug('Exiting CS')
    y = -1
    B[self.index] = 0
    #make the thread sleep for a good 3 seconds! lucky one gets to sleep more!
    time.sleep(3)
    
    
#global cs function 
def cs():
    logging.debug('Entering CS')

# method which calls the constructor of the Fast class and invokes the threads    
def spawnThreads(assign):
   
    i = 0
    global totalRequests
    
    for z in assign:
        totalRequests+=z
        Threads.append(Fast("THREAD", i, z))
        i+=1
    
    for each in Threads:
        if each.requests > 0:
            runningThreads.append(each)
            each.start()
    # wait until all the threads are done with their requests, then exit   
    for each in runningThreads:
        each.join()
        
        
        
       
