

name -          CHIRANJEEVI BALAWAT
id -            108147146
course code -   CSE690
assignment 2 
date -          3/6/12
time -          3.27 pm

/*-----------------------------------------------------------------Instructions and  details------------------------------------------------------------*/


################################################################  CONCURRENT ALGORITHM IMPLEMENTATION  ###################################################

the Fast mutual exclusion algorithm is in file 'Fast.py' and the Bakery algorithm is in file 'Bakery.py'. the driver program is named 'main.py'. to invoke the main program, execute the following on the terminal at the main.py file's location, all the above 3 files must be in the same directory

Python main.py n m

n - number of processes
m - number of threads

the main .py file randomly distributes m requests among the n threads, stores them in a list 'assign'. the list's index represents the thread and the value represents the allotted requests for that particular thread. it then calls the 'spawnthreads' global function, which exists in each of the 'Fast.py', 'Bakery.py' files.the 'spawnthreads' function actually creates the threads, initializes its variables - requests, threadname, index of each thread, using the constructor of the Fast class, Fast class inherits the Thread.threading class. the execution is illustrated as follows,

Running Lamport's fast mutual exclusion algorithm

.
.
.


Running Lamport's Bakery algorithm

.
.
.


please find attached the sample output obtained for each of the algorithms, for 100 threads and 50 requests.

the cs() function has been defined as a global one as I was not able to figure out how to implement the same inside a class. according to my implementation, the thread which gains access to cs, invokes the cs() and prints out a message saying 'in cs' and returns back to the calling function contend() and prints 'exiting cs' from contend().

the requestmanager() function keeps track of the satisfied and unsatisfied requests of each and every thread and allows a thread to 'contend()' for 'cs()' if it has any unsatisfied requests, and also prevents a thread from trying to access the cs() when it has satisfied all its requests. I have used the thread.join() functionality which basically waits for each of the thread to finish satisfying its requests. 



#####################################################  DISTRIBUTED ALGORITHM IMPLEMENTATION  #############################################################



the ricart-agrawala algorithm is in file 'RAtoken.dis', the suzuki-kasami algorithm is in file 'SKtoken.dis'. to invoke each of the programs change directory to the location of the distalgo module and invoke the following..

- $Python3 -m distalgo.compiler /dirContainingThe .dis file RAtoken.dis                     ----------- 1
- $Python3 -m distalgo.runtime /dirContainingThe .dis file RAtoken.dis n m                  ----------- 2

- $Python3 -m distalgo.compiler /dirContainingThe .dis file SKtoken.dis                     ----------- 1
- $Python3 -m distalgo.runtime /dirContainingThe .dis file SKtoken.dis n m                  ----------- 2

n - number fo processes
m- number of requests.

The ricart-agrawala algorithm has been implemented as per the pseudocode given in the following link - 

https://sites.google.com/site/sbcscda/lectures/week-3 

the suzuki-kasami algorithm has been implemented as given in the attached file 'p344-suzuki.pdf' as i was not able to understand the pseudocode given at the same above mentioned link. 

if the n, m are not specified, then the code takes n = 10 and m = 27 as a default value. each of the .dis files upon exectution run as per the algorithm specifications, but have to be terminated manually. please press 'ctrl-z' to terminate the currently executing file [RAtoken.dis or SKtoken.dis] and run 1, 2 if you need to run the other .dis file. both the algorithms' implementation work fine for smaller values [<100] of n and m.

please find attached to the sample output obtained for each of the algorithms.

REFERENCES:

[1] http://docs.python.org/tutorial/
[2] http://dl.acm.org/citation.cfm?id=214406
[3] http://wikipedia.org                                ----- Used wikipedia to learn more about the control flow in the concurrent algorithms.

/*-------------------------------------------------------------------------------END--------------------------------------------------------------------*/

