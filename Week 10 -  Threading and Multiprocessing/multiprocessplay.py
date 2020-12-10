"""
    demonstrate the multiprocessing module
    using sleep and loop as done in threadplay.py

    user must set dosleep  and join_one_by_one

    if dosleep is true,  job1 and job2 call the sleep function
    else, job1 and job2 run a loop

    if joinafterreachstart is true,  joins are done immediately after each start, causing program to wait before next start
    else,  joins are done after all jobs have started

"""
import os
import time
import random
from multiprocessing import Process

def sleep_or_loop(index,dosleep):
    """
        simple function that prints when the thread starts and exits
        inbetween it waits two seconds
    """
    proc = os.getpid()
    if dosleep:
        sleeptime = 1
        time.sleep(sleeptime)
        print('index {0}:  by process id: {1}, sleeptime {2}'.format(index,proc,sleeptime))
    else:
        loopnum = 10000000
        for j in range(loopnum):
            pass
        print('index {0}:  by process id: {1}, loop'.format(index,proc))


if __name__ == '__main__':
    ## need to run inside __main__()
    ## see https://pymotw.com/2/multiprocessing/basics.html
    dosleep = False #True #False # false means to loop
    join_one_by_one = False #True #True # false means join after all have started


    print("dosleep:",dosleep,"  join_one_by_one:",join_one_by_one)

    starttime = time.time()
    numprocs = 4
    procs = []
    for index in range(numprocs):
        proc = Process(target=sleep_or_loop, args=(index,dosleep))
        procs.append(proc)
        print("starting",index)
        proc.start()
        if join_one_by_one:
            proc.join()

    if join_one_by_one is False:
        for proc in procs:
            proc.join()

    stoptime = time.time()
    print("duration",stoptime-starttime)

    dosleep = False #True #False # false means to loop
    join_one_by_one = False #True #True # false means join after all have started
