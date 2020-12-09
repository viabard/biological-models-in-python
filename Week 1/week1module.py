def logsum(values):
    """ values is a list of numbers
        add up the numbers in the list
        calculate the natural logarithm
        print the results"""
    import math
    addedup = sum(values)
    myresult = math.log(addedup)
    return (myresult)


def joinwords(wordlist):
    """ wordlist is a list of strings
        join the strings into a single string with a space as a separator"""
    return " ".join(wordlist)
