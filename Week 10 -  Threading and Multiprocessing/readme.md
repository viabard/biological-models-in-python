# Week 10 - Multiprocessing and Threading
Two part assignment, one having to do with threading, the other with multiprocessing. Checking times compared betweeen joining after each job and joining after all jobs.
This worksheet was made and is copyrighted (2020) by Dr. Jody Hey at Temple University

1. Part 1:

Write a program that:
- Measures how long it takes to run a set of 4 jobs using the thread module and then using the multiprocess module depending on when you call and join
- The program will take 2 command line arguments, one that specifies which module to use and one that specifies when to join
- Each job should involve:
    - Reading in a fasta file and making a list of SeqRecords (SeqIO or SeqParse module of BioPython)
    - Calculating the number of records in each list and the total sequence length for each file, and printing these values to the screen after the jobs have finished
    - Calculating the total run time from start to finish and printing the results to a file or to the screen
- The four files are: Myotis_aligned_small.fasta; opuntia.fasta; porcelaincrab_aligned.fasta; and pyrus.fasta
- Run your code from the command line for all 4 sets of starting conditions:
    - Threading module, calling join() after each job is started
    - Threading module, calling join() after all the jobs started
    - Multiprocess module, call join() after each job is started
    - Multiprocess module, call join() after all the jobs started

**Remember to run multiprocess within the condition "if __name__ == '__main__':" if you are using Windows