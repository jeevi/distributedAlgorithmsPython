
#---------------------------------Lamport's Bakery algorithm------------------------------------------#

import threading
import time
import logging
import random

# global variables
totalReq = 0 
Threads = []
runningThreads = []
choosing = [0]*100
num = [0]*100

# using the logging module from python's library which basically formats the output to be displayed on the console
logging.basicConfig(level=logging.DEBUG, format='[%(threadName)s, %(asctime)s, %(message)s]', datefmt = '%Y-%m-%d %H:%M:%S')

class Bakery(threading.Thread):
    
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
    global totalReq
    # keep doing until all the requests of all the threads have been satisfied
    while totalReq > 0:
        #if all the requests are satisfied - do nothing
        if self.requests == 0:
            pass
        # else do this
        else:
            contend(self)
        totalReq-=1
        
        
# a global function which contains the logic of the lamport's bakery algorithm
def contend(self):

    choosing[self.index] = 1
    num[self.index] = 1 + maxOfnum()
    choosing[self.index] = 0
    for each in Threads:
        while(not( choosing[each.index] == 0)):
            logging.debug('...')
        while (num[each.index] != 0) and ((num[each.index] < num[self.index]) or ((num[each.index] == num[self.index]) and (each.index < self.index))):
            logging.debug('...')
            
    #if  a thread is here, it has every right to enter CS and so it does!
    cs()
    num[self.index] = 0
    #make the thread sleep for a good 3 seconds! lucky one gets to sleep more!
    time.sleep(3)
          
        
def maxOfnum():

    curMax = -1
    global num
    
    for each in Threads:
        if num[each.index] > curMax:
            curMax = num[each.index]
    
    return curMax

#global cs function 
def cs():
    
    logging.debug('Entering CS')
    logging.debug('Exiting CS')
    
# method which calls the constructor of the Fast class and invokes the threads
def spawnThreads(assign):
   
    i = 0
    global totalReq
    
    for z in assign:
        totalReq+=z
        Threads.append(Bakery("BTHREAD", i, z))
        i+=1
    
    for each in Threads:
        if each.requests > 0:
            runningThreads.append(each)
            each.start()  
    # wait until all the threads are done with their requests, then exit
    for each in runningThreads:
        each.join()
