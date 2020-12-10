# Week 4 - Distributions and Weasel Program
Introduction to probability, play with probability distributions in python, and genetic algorithms.
This assignment had two parts.
This worksheet was made and is copyrighted (2020) by Dr. Jody Hey at Temple University

1. Part 1:

Write a program that simulates 1000 random values from a poisson distribution, an exponential distribution, and a normal distribution. 
- Us the following parameter values: Poisson - 5: Exponential - 0.5: Normal - 10,5
- You can use the numpy.random.poisson() for Poisson
    - This returns a numpy array, use the list() method to make a regular list from it
- You can use the random module for exponential and normal (aka Gaussian)
- For all three distributions, calculate the mean and the variance (or standard deviation) for the 1000 random variables
- Compare the mean and variance of your sample to the values expected for the expectation and variance of that kind of distribuation and the parameter(s) you used (researched)
- Write an output file showing results for all three distributions, with a final comparison of calculated mean and variance, and the values expected for those distributions

2. Part 2:

Write a weasel program to simulate "methinks it is like a weasel"
- Start by simulating a random string of 28 letter and spaces
- Create a loop to simulate new sequences:
    - Reproduce and Mutate: Make a new sequence by copying the current sequency, but with a chance of mistake (user specified). You can make one or more children.
    - Selection: Keep the new sequence if it is more similar to the target sequence, otherwise discard the new sequence (ties, keep original). If you've made more than one children, keep only the best one.