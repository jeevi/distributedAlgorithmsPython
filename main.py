
#----------------------------- this is the driver program--------------------------#

import Fast #needed so can invoke the Fast algorithm
import Bakery #needed so can invoke the Bakery algorithm
import random
import sys

if len(sys.argv)!=3:
    sys.exit("\n\nwrong number of arguments, usage: python randnum.py threads requests\n\n")
    
thr = int(sys.argv[1])
req = int(sys.argv[2])

#initialising a list whose index represents the thread and its value the number requests assigned to it
assign = [0]*thr

# randomly distributing the requests among the threads
while req:
    j = random.randrange(0, thr)
    assign[j]+=1
    req-=1

# just to check
for x in assign:
	print (x)

print ("\nRunning Lamport's fast mutual exclusion algorithm\n")
Fast.spawnThreads(assign)

print ("\n\nRunning Lamport's bakery algorithm\n\n")
Bakery.spawnThreads(assign)


    

