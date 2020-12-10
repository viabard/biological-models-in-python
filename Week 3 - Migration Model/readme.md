# Week 3 - Migration Model
This week there were two parts, each implementing an island migration model.
This worksheet was made and is copyrighted (2020) by Dr. Jody Hey at Temple University

1. Part 1:

Write a program to implement the island model of migration:
- Get from the user: P frequency on mainland, p0 frequency on the island in generation 0 (starting frequency), m, g the number of generations for which to calculate the next allele frequency
- Print to the screen: pt as t goes from 0 up to and including g

2. Part 2:

Write a program to implement the Island model of migration, but with a random change in allele frequency added to the dterministic value
- Get from the user: P frequency on mainland, p0 frequency on the island in generation 0 (starting frequency), m with a maximum value of 0.01, s random number seed (positive integer)
- Calculate pt for the next generation using the standard deterministic migration modeel (as in part 1)
    - Add to this value a random uniformly distribited value between -0.05 and 0.05
    - Continue the run until the pt is >= 1 (allele is fixed) or <= 0 (allele is lost)
    - Print to the screen the final frequency and the number of generations it took to get there.
- If the run takes more than 10,000 generations, stop the run and print the current allele frequency and a message that it is taking too long
