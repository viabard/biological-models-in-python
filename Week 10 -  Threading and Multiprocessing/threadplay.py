"""
    basic demonstration of running multiple threads,  each associated with a function

    user must set dosleep  and join_one_by_one

    dosleep sets whether or not the sleep_or_loop() function sleeps or loops

    if dosleep is true,
        sleep_or_loop() calls the sleep function and waits (not doing much)
    else
        sleep_or_loop() runs a loop  (busy busy)

    join_one_by_one sets when join() is called.

    join() is used to tell one thread to wait for another thread to finish.

    if joinafterreachstart is true,
        join() is called for each thread after it is started
        this caused the program to wait before the next start
    else
        joins are done after all jobs have started

    so 4 conditions to try:
            dosleep and join_one_by_one
            not dosleep and join_one_by_one
            dosleep and not join_one_by_one
            not dosleep and not join_one_by_one
"""
import threading
import time


def sleep_or_loop(dosleep):
    """
        simple function that prints when the thread starts and exits
        inbetween it waits two seconds
    """
    print(threading.current_thread().getName(), 'Starting')
    if dosleep:
        sleeptime = 1
        time.sleep(sleeptime)
    else:  ## loop
        loopnum = 10000000
        for j in range(loopnum):
            pass
    print(threading.current_thread().getName()," exiting")

dosleep = False #True #False # false means to loop, i.e. not sleep
join_one_by_one = False#True # false means join after all have started

numthreads = 10


starttime = time.time()
print("dosleep:",dosleep,"  join_one_by_one:",join_one_by_one)
t = [] # a list of threads
for i in range(numthreads):
    t.append(threading.Thread(name='thread_' + str(i) + "_job", target=sleep_or_loop, args = (dosleep,)))
    t[i].start()
    if join_one_by_one:
        t[i].join()

if join_one_by_one is False:
    for i in range(numthreads):
        t[i].join()

stoptime = time.time()

print("duration",stoptime-starttime)


